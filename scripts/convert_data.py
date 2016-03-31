import sys
sys.path.append('..')
import os
import json

from watson_developer_cloud import DocumentConversionV1

import private
import settings


if __name__ == '__main__':
    document_conversion = DocumentConversionV1(
        username=private.DOC_CONVERSION_USERNAME,
        password=private.DOC_CONVERSION_PASSWORD,
        version='2016-02-09')

    # Go through each Dataset and ingest into ElasticSearch
    for doc in settings.DOCS_2014_15:
        json_path = doc.path + '.json'
        if os.path.exists(json_path):
            print "{0} already exists. Skipping.".format(json_path)
            continue

        config = {}
        with open(doc.path) as document:
            config['conversion_target'] = DocumentConversionV1.ANSWER_UNITS
            document = document_conversion.convert_document(
                document=document, config=config)

            fh = open(json_path, 'w')
            doc_as_json = json.dumps(document, indent=4).replace(
                u'\xa0', u' ').replace('\u00a0', u' ')
            fh.write(doc_as_json)
