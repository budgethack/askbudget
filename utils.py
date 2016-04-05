from elasticsearch import Elasticsearch
import bleach

import private


def _sentence_ranker(item):
    if item.get('is_main'):
        return 3

    if item.get('is_sub'):
        return 2

    return 1


def handle_agg(text=None):
    query = {
        'size': 10,
        'query': {
            'bool': {
                'filter': [{'term': {'year': '2015-16'}}]
            }
        },
        'aggs': {
            'by_doc': {
                'terms': {
                    'field': 'doc_name'
                }
            },
            'entity_keywords': {
                'significant_terms': {
                    'field': 'keywords.text'
                }
            },
            'entities': {
                'significant_terms': {
                    'field': "entities.text",
                }
            },
            'main_concepts': {
                'significant_terms': {
                    'field': 'concepts.text',
                    'size': 50
                }
            }
        },
        'highlight': {
            "pre_tags" : ["<mark>"],
            "post_tags" : ["</mark>"],
            'fields': {
                'aug_sentences.text': {},
                'text': {},
                'concepts.text': {'number_of_fragments': 0}
            }
         }
    }

    global_query = None

    if text:
        query['query']['bool'] = {
            'must': [{
                'multi_match': {
                    'fields': ['text^2', 'concepts.text', 'aug_sentences.text^2'],
                    'query': text,
                    'operator': 'and'
                }
            }],
        }

        global_query = {
            'size': 0,
            'query': {
                'multi_match': {
                    'fields': ['text^2', 'concepts.text'],
                    'query': text
                }
            },
            'aggregations': {
                'historic_mentions': {
                    'terms': {
                        'field': 'year',
                        'size': 5
                    }
                }
            }
        }


    output = {}

    es = Elasticsearch([private.ELASTICSEARCH_HOST])
    result = es.search(body=query, index='budgethack')
    if global_query:
        global_result = es.search(body=global_query, index='budgethack')
        output['historic_mentions'] = [{
            'year': b['key'], 'count': b['doc_count']}
            for b in global_result['aggregations']['historic_mentions']['buckets']]


    output['top_mentions'] = parse_top_mentions(result)
    output['related_things'] = parse_related_things(result)
    output['related_spend'] = parse_related_spend(result)
    output['main_concepts'] = parse_main_concepts(result)

    return output

def parse_related_things(result):
    output = {}
    output['keywords'] = []
    for keyword in result['aggregations']['entity_keywords']['buckets']:
        output['keywords'].append({
            'name': keyword['key'],
            'count': keyword['doc_count']
        })

    return output


def parse_top_mentions(result):
    output = {
        'count': result['hits']['total'],
        'docs': []
    }

    for agg in result['aggregations']['by_doc']['buckets']:
        output['docs'].append({
            'name': agg['key'], 'count': agg['doc_count']})

    return output


def parse_related_spend(result):
    output = {}

    top_sentences = []
    top_sentences_raw = set([])

    aug_sentences = []
    is_concept = False

    seen_sentences = set([])

    for result in result['hits']['hits']:
        if 'concept.text' in (result.get('highlight') or {}):
            is_concept = True

        for sentence in result['_source'].get('aug_sentences') or []:
            text = sentence['text']
            if text in seen_sentences:
                continue

            seen_sentences.add(text)

            text = text.replace('The Budget includes: ', '')
            text = text.replace('The Budget provides ', '')
            text = text.replace('The Andrews Labor Government is investing ', '')
            text = text.replace('The Budget invests ', '')
            text = text.replace('The Budget commits ', '')
            text = text.replace('The Budget also provides ', '')

            for highlight in (result.get('highlight') or {}).get('aug_sentences.text') or []:
                text = text.replace(bleach.clean(highlight, strip=True), highlight)

            for entity in sentence['entities']:
                if entity['type'] == 'Quantity':
                    text = text.replace(entity['text'], u'<strong>{0}</strong>'.format(entity['text']))

            sentence['text'] = text
            sentence['doc_name'] = result['_source']['doc_name']
            sentence['doc_url'] = result['_source']['doc_url']
            top_sentences.append(sentence)

    output['docs'] = sorted(top_sentences, key=_sentence_ranker, reverse=True)[:3]
    output['is_concept'] = is_concept

    return output


def parse_main_concepts(result):
    output = {'docs': []}

    for agg in result['aggregations']['main_concepts']['buckets']:
        output['docs'].append({'text': agg['key'], 'count': agg['doc_count']})

    return output


def parse_word_count(result):
    output = {}
    output = result 

    return output
