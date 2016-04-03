import os
import json

import nltk.data
from elasticsearch import Elasticsearch

import private
import settings


if __name__ == '__main__':
    es = Elasticsearch([private.ELASTICSEARCH_HOST])

    if not es.indices.exists(settings.INDEX_NAME):
        es.indices.create(settings.INDEX_NAME, body={
            'mappings': {
                'doc': {
                    'properties': {
                        'year': {
                            'type': 'string',
                            'index': 'not_analyzed'
                        },
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

    for year, docs in settings.DOCS.items():

        for doc in docs:
            json_path = doc.path + '.json'
            if not os.path.exists(json_path):
                print (
                    "{0} is missing. "
                    "Ensure you have run the ``convert_data.py`` script first")
                continue

            config = {}
            with open(json_path) as doc_fh:
                document = json.loads(doc_fh.read())

                for answer in document['answer_units']:
                    title = answer['title']
                    text = answer['content'][0]['text'].replace(u'\xa0', u' ')
                    section_type = answer['type']
                    sentences = tokenizer.tokenize(text)
                    print "Working."
                    es.index(
                        body=dict(
                            year=year,
                            doc_url=doc.url, doc_name=doc.name,
                            title=title, text=text, section_type=section_type,
                            sentences=sentences),
                        index=settings.INDEX_NAME, doc_type='doc')
