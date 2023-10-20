#!/usr/bin/env python3
'''Task No. 8 module.
'''


def list_all(mongo_collection):
    """
    printing list of collections otherwise empty lisi
    """
    return [doc for doc in mongo_collection.find()]
