#!/usr/bin/env python3
"""Module that provides a function to list all documents in a collection."""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        list: List of documents in the collection. Empty list if none.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
