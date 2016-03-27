from collections import namedtuple

from elasticsearch import Elasticsearch

from watson_developer_cloud import DocumentConversionV1

import private


BudgetDocument = namedtuple('BudgetDocument', ['name', 'path', 'url'])

INDEX_NAME = 'budgethack'
DATASET_DIR = 'datasets'

DOCS = [
    BudgetDocument(
        name='BudgetOverview',
        path='datasets/2015-16/BudgetOverview.pdf',
        url='http://www.dtf.vic.gov.au/files/7e68011b-a770-4d23-bf61-a48200c2de10/BudgetOverview.pdf'),  # noqa
    BudgetDocument(
        name="TreasurersSpeech",
        path='datasets/2015-16/BP1-2015-16.pdf',
        url='http://www.dtf.vic.gov.au/files/a1ddaa97-9692-426c-aff6-a48200c2d9d9/BP1-2015-16.pdf'),  # noqa
    BudgetDocument(
        name='Putting People First',
        path='datasets/2015-16/BIP_PuttingPeopleFirst.pdf',
        url='http://www.dtf.vic.gov.au/files/a5924d7a-3777-46ee-ba19-a48200c801ab/PuttingPeopleFirst.pdf'),  # noqa
    BudgetDocument(
        name='Getting On With It',
        path='datasets/2015-16/BIP_GettingOnWithIt.pdf',
        url='http://www.dtf.vic.gov.au/files/24da5c15-d12d-49ba-840c-a48200c2ded4/GettingOnWithIt.pdf'),  # noqa
    BudgetDocument(
        name='Rural and Regional',
        path='datasets/2015-16/BIP_RuralandRegional.pdf',
        url='http://www.dtf.vic.gov.au/files/1a567685-5d19-4507-96c8-a48200c2e018/RuralandRegional.pdf'),  # noqa
    BudgetDocument(
        name='Suburban Growth',
        path='datasets/2015-16/BIP_SuburbanGrowth.pdf',
        url='http://www.dtf.vic.gov.au/files/98ec13c0-9e77-4f48-9716-a48200c802ee/SuburbanGrowth.pdf')  # noqa
]


if __name__ == '__main__':
    es = Elasticsearch()
    es.indices.delete('budgethack')

    document_conversion = DocumentConversionV1(
        username=private.DOC_CONVERSION_USERNAME,
        password=private.DOC_CONVERSION_PASSWORD,
        version='2016-02-09')

    # Go through each Dataset and ingest into ElasticSearch
    for doc in DOCS:
        config = {}
        with open(doc.path) as document:
            config['conversion_target'] = DocumentConversionV1.ANSWER_UNITS
            document = document_conversion.convert_document(
                document=document, config=config)

            for answer in document['answer_units']:
                title = answer['title']
                text = answer['content'][0]['text'].replace(u'\xa0', u' ')
                section_type = answer['type']
                es.index(body=dict(
                    doc_url=doc.url,
                    title=title, text=text, section_type=section_type),
                    index='budgethack', doc_type=doc.name)
