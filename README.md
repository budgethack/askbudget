AskBudget
-----------

Budget Hack Team:

Damon Toumbourou

Idea
-----

The simplest possible way to ask questions about your budget. Submit a question and we'll do our best to answer it automatically. Also, see other questions people have asked.

Plan
-----

1. Use ``PDFMiner`` to extract text from documents:

```
Budget Overview (BudgetOverview.pdf)
Budget Speech (BudgetSpeech.pdf)
Strategy and Outlook (BP2-2015-16.pdf)
```

2. Break each document down into subsections.
3. For each subsection, perform Entity Detection.
4. Store each document fragment in Elasticsearch along with the learned ideas.
5. Build front end that can query the index and return key ideas along with some interesting aggregates.

API endpoints
--------

```GET /api/question```

Used for asking a question to Budget.

Query params:

  * ``question <string> - question text``

Response:

   * ``answers <list> - a list of answers``

Example request:

```
GET /api/question?question=Does+the+budget+deliver+a+surplus?
```

Example response:
```
{
   "question": {"Does the budget deliver a surplus?",
   "answers": [{
       "text_fragment": "the Budget produces a strong operating surplus of $1.2 billion and it reduces net debt to 4.4 per cent of gross state product (GSP) by June 2011",
       "document_name": "BudgetOverview.pdf"
   }]
}
```
