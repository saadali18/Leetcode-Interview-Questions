# Description: This file contains the solution to the LRU Cache problem.

# Problem Statement
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Best Explaination: https://youtu.be/xDEuM5qa0zg?si=bCyLViWIdKZtS5yp

# Solution 1: Using stack and dictionary

# Time Complexity: O(n) for both get and O(1) for put operation

# Space Complexity: O(n) where n is the capacity of the cache


class LRUCacheUsingStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the top of the stack
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            # Remove the least recently used key from the stack and cache
            lru_key = self.stack.pop(0)
            del self.cache[lru_key]

        # Add the new key to the top of the stack and update the cache
        self.stack.append(key)
        self.cache[key] = value


# Example Usage
lru_cache = LRUCacheUsingStack(2)

lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # Output: 1
lru_cache.put(3, 3)  # Remove the least recently used key (2)
print(lru_cache.get(2))  # Output: -1 (not found)
print(lru_cache.get(3))  # Output: 3