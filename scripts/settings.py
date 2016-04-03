from collections import namedtuple


BudgetDocument = namedtuple('BudgetDocument', ['name', 'path', 'url'])

INDEX_NAME = 'budgethack'
DATASET_DIR = 'datasets'

DOCS = {
    '2015-16': [
        BudgetDocument(
            name='Budget Overview',
            path='datasets/2015-16/BudgetOverview.pdf',
            url='http://www.dtf.vic.gov.au/files/7e68011b-a770-4d23-bf61-a48200c2de10/BudgetOverview.pdf'),  # noqa
        BudgetDocument(
            name="Treasurer's Speech",
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
    ],
    '2014-15': [
        BudgetDocument(
            name='Budget Overview',
            path='datasets/2014-15/BudgetOverview.pdf',
            url='http://www.dtf.vic.gov.au/files/90f08639-26b1-45b9-957e-a49c00a46994/Budget-Overview-2014-15.pdf')
    ]
}
