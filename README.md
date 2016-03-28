AskBudget
========

Idea
-----

The simplest possible way to ask questions about your budget. Submit a question and we'll do our best to find the most important information from the budget papers.

Team
----

* Damon Toumbourou
* Lucy Wood
* Lex Toumbourou
* Su Myat
* Ben Diep
* Alex Cheong

How it works
------------

1. We convert all documents to raw using Watson's Document Converted and index them into Elasticsearch. (see ``scripts/ingest_data.py``).
2. On each document, we perform Entity Detection using Alchemy's API and store the results back into Elasticsearch (see ``scripts/entity_detection.py``).
3. When a search term is submitted to the front end, we perform a bunch of Elasticsearch aggregtations to attempt to find the most interesting results.

Setup
-----

You will need:

1. An Elasticsearch instance.
2. A Watson API key for Alchemy and Document Converted.

Setup:

1. Clone repo.
2. In cloned repo, create a virtualenv and run:

```
(someenv)> pip install -r requirements.
```

3. Then, install front end components with Bower:

```
(someenv)> bower install
```

API endpoints
--------

```POST /api/question```

Used for creating a new Budget question.
