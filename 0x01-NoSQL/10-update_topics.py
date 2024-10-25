#!/usr/bin/env python3
"""
Module Name: school_db
Description: This module provides a function to update the topics of a school document in a MongoDB collection based on the school's name.
"""
def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school's name.
    
    Args:
        mongo_collection: The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.
    
    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
