#!/usr/bin/env python3
"""
Cache module that interacts with Redis for storing and retrieving data,
with support for conversion functions.
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int]]:
        """
        Retrieve the value stored in Redis for the given key and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve the value from Redis.
            fn (Optional[Callable]): A function to apply to the retrieved value for conversion.

        Returns:
            Optional[Union[str, bytes, int]]: The retrieved value, possibly converted by fn,
                                              or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the value stored in Redis and decode it to a UTF-8 string.

        Args:
            key (str): The key to retrieve the value from Redis.

        Returns:
            Optional[str]: The retrieved value as a string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the value stored in Redis and convert it to an integer.

        Args:
            key (str): The key to retrieve the value from Redis.

        Returns:
            Optional[int]: The retrieved value as an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)


# Example usage:
if __name__ == "__main__":
    cache = Cache()

    # Testing with different types of data and functions
    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
