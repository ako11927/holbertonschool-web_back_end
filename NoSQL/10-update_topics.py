#!/usr/bin/env python3
"""Module for updating topics of a school document by name."""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): school name to update.
        topics (list of str): list of topics to set.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
