#!/usr/bin/env python
from requests_batch import Batching
from pprint import pprint

with Batching("http://localhost:5000/batch") as b:
    alice = b.patch("/person/alice", json={"favorite_food": "panang curry"})
    bob = b.patch("/person/bob", json={"favorite_food": "butter chicken"})

pprint(alice)
pprint(alice.json())

pprint(bob)
pprint(bob.json())
