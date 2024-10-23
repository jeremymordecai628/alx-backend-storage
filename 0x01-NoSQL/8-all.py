#!/usr/bin/env python3
"""
This lists all documents in a collection using Python
"""


def list_all(mongo_collection):
    """
    This function lists all documents in a collection
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents