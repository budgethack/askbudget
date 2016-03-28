from elasticsearch import Elasticsearch


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
            }
        }
    }
    es = Elasticsearch()
    result = es.search(body=query, index='budgethack')

    output = {}
    output['top_mentions'] = parse_top_mentions(result)
    output['related_things'] = parse_related_things(result)
    
    return output


def parse_related_things(result):
    output = {}
    output['keywords'] = []
    for keyword in result['aggregations']['entity_keywords']['buckets'][:8]:
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


#def find_related_spend(result):
#    output['related_spend'] = {'mentions': []}
#    for hit in result['hits']['hits']:
#        for entity in hit['_source'].get('entities') or []:
#            if (
#                entity['type'] == 'Quantity' and
#                entity['text'].startswith('$') and
#                ('mill' in entity['text'] or 'bill' in entity['text'])
#            ):
#                appended = entity
#                output['related_spend']['mentions'].append(appended)
#
#    output['related_spend']['mentions'] = (
#        output['related_spend']['mentions'][:5])
#
#    return output
