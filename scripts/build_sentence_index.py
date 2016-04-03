import sys
sys.path.append('..')

from watson_developer_cloud import AlchemyLanguageV1

from elasticsearch.helpers import scan
from elasticsearch import Elasticsearch

import settings
import private

import re

def parse_quantity(quantity):
    multiplier = None
    dollar = None
    result = re.findall(r'(\d+) (million|billion)', '$16 billion')
    if result:
        dollar = result[0][0]
        if result[0][1] == 'million':
            multiplier = 1000000
        elif result[0][1] == 'billion':
            multiplier = 1000000000
    if multiplier and dollar:
        return int(dollar) * multiplier
    

if __name__ == '__main__':
    es = Elasticsearch([private.ELASTICSEARCH_HOST])
    query = {
        'query': {
            'bool': {
                'filter': [{'term': {'year': '2015-16'}}]
            }
        }
    }

    al = AlchemyLanguageV1(api_key=private.ENTITY_API_KEY)
    combined_operations = ['entity', 'keyword', 'taxonomy', 'concept']

    for hit in scan(es, query=query, index=settings.INDEX_NAME):
        source = hit['_source']
        
        aug_sentences = []
        for sentence in hit['_source'].get('sentences') or []:
            data = {}
            if 'the budget' in sentence.lower() and '$' in sentence:
                data['is_main'] = True
            elif '$' in sentence:
                data['is_sub'] = True

            result = al.combined(
                text=sentence, extract=combined_operations,
                sentiment=True)

            quantities = []
            for entity in result['entities']:
                if entity['type'] == 'Quantity':
                    entity['amount'] = parse_quantity(entity['text'])
                    quantities.append(entity)

            data.update(result)
            data['text'] = sentence
            data['quantities'] = quantities

            aug_sentences.append(data)

        source['aug_sentences'] = aug_sentences

        print u"Reindexing doc: {0}".format(hit['_id'])
        es.index(
            id=hit['_id'], index='budgethack',
            doc_type=hit['_type'], body=source)
