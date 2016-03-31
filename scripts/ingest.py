import sys
sys.path.append('..')
import os
import json

import nltk.data
from elasticsearch import Elasticsearch

import private
import logging
import settings


if __name__ == '__main__':
    es = Elasticsearch()
    es.indices.create('budgethack', body={
        'mappings': {
            'doc': {
                'properties': {
                    'doc_name': {
                        'type': 'string',
                        'index': 'not_analyzed'
                    },
                    'concepts': {
                        'properties': {
                            'text': {
                                'type': 'string',
                                'index': 'not_analyzed'
                            }
                        }
                    },
                    'keywords': {
                        'properties': {
                            'text': {
                                'type': 'string',
                                'index': 'not_analyzed'
                            }
                        }
                    },
                    'taxonomy': {
                        'properties': {
                            'text': {
                                'type': 'string',
                                'index': 'not_analyzed'
                            }
                        }
                    },
                    'entities': {
                        'properties': {
                            'text': {
                                'type': 'string',
                                'index': 'not_analyzed'
                            },
                            'type': {
                                'type': 'string',
                                'index': 'not_analyzed'
                            }
                        }
                    }
                }
            }
        }
    })
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Go through each Dataset and ingest into ElasticSearch
    for doc in settings.DOCS_2014_15:
        json_path = doc.path + '.json'
        if not os.path.exists(json_path):
            print "{0} is missing. Ensure you have run the ``convert_data.py`` script first"
            continue

        config = {}
        with open(json_path) as doc_fh:
            document = json.loads(doc_fh.read())
            
            for answer in document['answer_units']:
                title = answer['title']
                text = answer['content'][0]['text'].replace(u'\xa0', u' ')
                section_type = answer['type']

                sentences = tokenizer.tokenize(text)
                es.index(body=dict(
                    doc_url=doc.url, doc_name=doc.name,
                    title=title, text=text, section_type=section_type,
                    sentences=sentences), index='budgethack', doc_type='doc')
