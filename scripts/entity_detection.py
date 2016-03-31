import nltk.data

from watson_developer_cloud import AlchemyLanguageV1

from elasticsearch.helpers import scan
from elasticsearch import Elasticsearch

import private

if __name__ == '__main__':
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    es = Elasticsearch()
    al = AlchemyLanguageV1(api_key=private.ENTITY_API_KEY)
    combined_operations = ['entity', 'keyword', 'taxonomy', 'concept']

    for hit in scan(es, index='budgethack'):
        source = hit['_source']

        if hit['_source']['text']:
            result = al.combined(
                text=hit['_source']['text'], extract=combined_operations,
                sentiment=True)
            source.update(result)
            es.index(
                id=hit['_id'], index='budgethack',
                doc_type=hit['_type'], body=source)
