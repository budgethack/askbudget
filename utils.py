from elasticsearch import Elasticsearch

import private


def handle_text(text):
    query = {
        'size': 10,
        'query': {
            'match_phrase': {'text': text}
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
                    'field': 'concepts.text'
                }
            }
        }
    }
    es = Elasticsearch([private.ELASTICSEARCH_HOST])
    result = es.search(body=query, index='budgethack')

    output = {}
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
