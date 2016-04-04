import sys
sys.path.append('..')
import nltk.data

from watson_developer_cloud import AlchemyLanguageV1

from elasticsearch.helpers import scan
from elasticsearch import Elasticsearch

import private

import shelve

if __name__ == '__main__':
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    cache = shelve.open('./entity-cache')

    es = Elasticsearch([private.ELASTICSEARCH_HOST])
    al = AlchemyLanguageV1(api_key=private.ENTITY_API_KEY)
    combined_operations = ['entity', 'keyword', 'taxonomy', 'concept']

    for hit in scan(es, index='budgethack'):
        source = hit['_source']
        text = hit['_source']['text']
        
        print 'working...'
        if text:
            if not cache.has_key(text.encode('utf8')):
                try:
                    result = al.combined(
                        text=hit['_source']['text'], extract=combined_operations,
                        sentiment=True)
                except Exception as e:
                    print "Error occured. Skipping. ({0})".format(e)
                    continue
                cache[text.encode('utf8')] = result

            source.update(cache[text.encode('utf8')])
            print "ABOUT TO INGEST", source
            es.index(
                id=hit['_id'], index='budgethack',
                doc_type=hit['_type'], body=source)
