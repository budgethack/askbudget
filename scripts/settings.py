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
            url='http://www.dtf.vic.gov.au/files/90f08639-26b1-45b9-957e-a49c00a46994/Budget-Overview-2014-15.pdf'), 
		BudgetDocument(
			name='Strategy and Outlook',
			path='datasets/2014-15/Strategy-and-Outlook.pdf',
			url='http://www.dtf.vic.gov.au/files/7d64f872-b802-43dc-bb5f-a325009eca4e/Strategy-and-Outlook.pdf'),
		BudgetDocument(
			name='State Capital Program',
			path='datasets/2014-15/State-Capital-Program.pdf',
			url='http://www.dtf.vic.gov.au/files/fceae90c-24d6-42ee-9a88-a325009f6ade/State-Capital-Program.pdf'),
		BudgetDocument(
			name='Regional and Rural Victoria',
			path='datasets/2014-15/Regional-and-Rural-Victoria.pdf',
			url='http://www.dtf.vic.gov.au/files/9984a01c-2a11-478b-92fd-a325009ff19c/Budget-Information-Paper-Regional-and-Rural-Victoria.pdf'),
		BudgetDocument(
			name="Treasurer's Speech",
			path='datasets/2014-15/BP1-2014-15.pdf',
			url='http://www.dtf.vic.gov.au/files/d0395eb5-d778-4c99-947e-a325009e6642/Treasurers-Speech.pdf')
	],
	'2013-2014': [
        BudgetDocument(
            name='Budget Overview',
            path='datasets/2013-14/BudgetOverview2013-14.pdf',
            url='http://www.dtf.vic.gov.au/files/e926b98b-ca12-4083-9757-a1d200d9431d/BudgetOverview2013-14.pdf'),
		BudgetDocument(
			name='Infrastructure',
			path='datasets/2013-14/Infrastructure2013-14.pdf',
			url='http://www.dtf.vic.gov.au/files/bdf097d7-92be-4088-8f75-a1d200e4e435/Infrastructure2013-14.pdf'),
		BudgetDocument(
			name='Regional',
			path='datasets/2013-14/Regional2013-14.pdf',
			url='http://www.dtf.vic.gov.au/files/66a02ca5-b56e-476b-bcba-a1d200e36471/Regional2013-14.pdf'),
		BudgetDocument(
			name="Treasurer's Speech",
			path='datasets/2013-14/BP12013-14.pdf',
			url='http://www.dtf.vic.gov.au/files/84cacec1-eeb7-4c14-9673-a1d200d99a46/BP12013-14.pdf'),
		BudgetDocument(
			name='State Capital Program',
			path='datasets/2013-14/BP42013-14.pdf',
			url='http://www.dtf.vic.gov.au/files/393594ad-7cd8-4ae4-89af-a1d200e0e0c3/BP42013-14.pdf')
	],
	'2012-2013': [
        BudgetDocument(
            name='Budget Overview',
            path='datasets/2012-13/BudgetOverview2012-13.pdf',
            url='http://www.dtf.vic.gov.au/files/815b6261-aecf-434d-80f7-a308011f156c/BudgetOverview2012-13.pdf'),
		BudgetDocument(
			name='Family',
			path='datasets/2012-13/Family2012-13.pdf',
			url='http://www.dtf.vic.gov.au/files/aba45297-2071-45d9-a9b6-a308011f161e/Family2012-13.pdf'),
		BudgetDocument(
			name='Regional',
			path='datasets/2012-13/Regional2012-13.pdf',
			url='http://www.dtf.vic.gov.au/files/6f7748a4-6728-417f-b207-a308011f172a/Regional2012-13.pdf'),
		BudgetDocument(
			name="Treasurer's Speech",
			path='datasets/2012-13/BP12012-13.pdf',
			url='http://www.dtf.vic.gov.au/files/9f42bc1e-4779-4525-9337-a308011f133a/BP12012-13.pdf'),
		BudgetDocument(
			name='Strategy and Outlook',
			path='datasets/2012-13/BP22012-13.pdf',
			url='http://www.dtf.vic.gov.au/files/c4554df0-2d2e-4cb4-a676-a308011f13d0/BP22012-13.pdf'),
		BudgetDocument(
			name='Service Delivery',
			path='datasets/2012-13/BP32012-13.pdf',
			url='http://www.dtf.vic.gov.au/files/478abb0a-428c-4be8-81d1-a308011f1403/BP32012-13.pdf')	
	],
	'2011-2012': [
        BudgetDocument(
            name='Budget Overview',
            path='datasets/2011-12/BudgetOverview2011-12.pdf',
            url='http://www.dtf.vic.gov.au/files/e6806cf3-35f6-475f-882b-a33e00f6babd/BudgetOverview2011-12.pdf'),
		BudgetDocument(
			name="Treasurer's Speech",
			path='datasets/2011-12/BP12011-12.pdf',
			url='http://www.dtf.vic.gov.au/files/b04a9877-5831-46f1-b577-a33e00f69e36/BP12011-12.pdf'),
		BudgetDocument(
			name='Strategy and Outloook',
			path='datasets/2011-12/BP22011-12.pdf',
			url='http://www.dtf.vic.gov.au/files/ff401f44-4862-42b8-97ca-a33e00f6a103/BP22011-12.pdf'),
		BudgetDocument(
			name='State Capital Program',
			path='datasets/2011-12/BP42011-12.pdf',
			url='http://www.dtf.vic.gov.au/files/23bb729d-0f95-4901-8fed-a33e00f6b4f4/BP42011-12.pdf'),
		BudgetDocument(
			name='Statement of Finances',
			path='datasets/2011-12/BP52011-12.pdf',
			url='http://www.dtf.vic.gov.au/files/288e95e2-cb9c-4573-9e87-a33e00f6b7dd/BP52011-12.pdf'),
		BudgetDocument(
			name='Service Delivery',
			path='datasets/2011-12/BP32011-12.pdf',
			url='http://www.dtf.vic.gov.au/files/4d131c4a-f810-491b-be9c-a33e00f6a3d0/BP32011-12.pdf')	
	],
	'2010-2011': [
        BudgetDocument(
            name='Budget Overview',
            path='datasets/2010-11/BudgetOverview2010-11.pdf',
            url='http://www.dtf.vic.gov.au/files/e21131c6-c41d-4da8-bba0-a33e010eb521/BudgetOverview2010-11.pdf'),
		BudgetDocument(
			name="Treasurer's Speech",
			path='datasets/2010-11/BIP12010-11.pdf',
			url='http://www.dtf.vic.gov.au/files/5f26be43-5236-47d1-9670-a33e010eaa12/BP12010-11.pdf'),
		BudgetDocument(
			name='Strategy and Outlook',
			path='datasets/2010-11/BIP22010-11.pdf',
			url='http://www.dtf.vic.gov.au/files/6e6b0735-63dd-491b-a2e4-a33e010eacc7/BP22010-11.pdf'),
		BudgetDocument(
			name='Service Delivery',
			path='datasets/2010-11/BP32010-11.pdf',
			url='http://www.dtf.vic.gov.au/files/e4d39b21-e376-4b71-80cf-a33e010eaf7d/BP32010-11.pdf'),
		BudgetDocument(
			name='Statement of Finances',
			path='datasets/2010-11/BP42010-11.pdf',
			url='http://www.dtf.vic.gov.au/files/dd544849-ed9f-4d74-a05e-a33e010eb24f/BP42010-11.pdf')	
	]
}


