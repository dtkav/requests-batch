Requests-Batch
===========

|Travis CI build status| |GitHub license| |Latest Version|

*Batch multiple requests at the http layer.* Requests-Batch is inpsired by
`how google cloud storage does
batching <https://cloud.google.com/storage/docs/json_api/v1/how-tos/batch>`__.

The Requests-Batch client works well with APIs that implement HTTP batching.
See examples/google_storage_client.py for an example that interacts with the
Google storage batch API.

Requests-Batch's Batching class acts just like a requests session, except
that your requests are batched up into a single HTTP request using the
``multipart/mixed`` content type.


Installation
============

.. code:: bash

    pip install Requests-Batch


Getting Started
===============

You can use the Batching class just like a requests session.

.. code:: python

    from requests_batch import Batching

    alice_data = bob_data = {"example": "json"}

    with Batching("http://localhost:5000/batch") as s:
        alice = s.patch("/people/alice/", json=alice_data)
        bob = s.patch("/people/bob/", json=bob_data)

    alice         # <Response [200]>
    alice.json()  # {"response": "json"}

Why Batch?
==========

Often the round-trip-time from a client to a server is high. Batching
requests reduces the penalty of a high RTT, without the added complexity
of request parallelization.

.. figure:: sequence-diagram.svg
   :alt: 

Status
======

This project is in ``alpha``. I'm hoping to eventually get it approved
as a requests extension.

.. |Travis CI build status| image:: https://api.travis-ci.org/dtkav/requests-batch.svg?branch=master
   :target: https://travis-ci.org/dtkav/requests-batch/
.. |GitHub license| image:: https://img.shields.io/github/license/dtkav/requests-batch.svg
   :target: https://github.com/dtkav/requests-batch/blob/master/LICENSE
.. |Latest Version| image:: https://img.shields.io/pypi/v/requests-batch.svg
   :target: https://pypi.python.org/pypi/requests-batch
