#!/usr/bin/python3
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
