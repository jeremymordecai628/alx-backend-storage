#!/usr/bin/env python3
"""
Module Name: school_db
Description: This module provides a function to retrieve a list of schools that have a specific topic in a MongoDB collection.
"""
def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools that have a specific topic.
    
    Args:
        mongo_collection: The MongoDB collection object.
        topic (str): The topic to search for in schools' topics.
    
    Returns:
        A list of school documents matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
