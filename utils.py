static/js/app.js
from elasticsearch import Elasticsearch

import private


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
        }
    }

    global_query = None

    if text:
        query['query']['bool'] = {
            'must': [{
                'multi_match': {
                    'fields': ['text^2', 'concepts.text'],
                    'query': text
                }
            }]
        }

        global_query = {
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
    for result in result['hits']['hits']:
        for sentence in result['_source'].get('sentences') or []:
            if 'the budget' in sentence.lower() and '$' in sentence:
                if sentence not in top_sentences:
                    top_sentences.append({'text': sentence})

    output['docs'] = top_sentences[:3]

    return output


def parse_main_concepts(result):
    output = {'docs': []}

    for agg in result['aggregations']['main_concepts']['buckets']:
        output['docs'].append({'text': agg['key'], 'count': agg['doc_count']})

    return output


def parse_word_count(result):
    output = {}
    print result 
    output = result 

    return output
