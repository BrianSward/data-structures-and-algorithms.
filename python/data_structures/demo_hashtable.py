# Set:

# We are given a key - value pair
# 1. hash the key
# 2. find the corresponding index of the bucket
# 3. add the key - value pair to that bucket

# Get:

# We are given just a key
# 1. hash the key
# 2. find index of bucket
# 3. traverse the bucket and return the value

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        if not self.head:
            return "NULL"
        current = self.head
        string = ""
        while current:
            string += str(current.value) + " -> "
            current = current.next
        string += "NULL"
        return string

    def insert(self, item):
        old = self.head
        self.head = Node(item)
        self.head.next = old


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        """
        takes in string called key and returns an interger representing an index of buckets
        """
        hash = 0
        for char in key:
            hash += ord(char)
        # hash represents index of bucket in hash table
        hash = (hash * 19) % self.size
        return hash

    def set(self, key, value):
        """
        Given a key value pair, hash the key, and insert pair into correct bucket
        """
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        if not bucket:
            self._buckets[hashed_key] = LinkedList()
        # now that self._buckets[hashed_key] is a linked list we can use insert
        self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        """
        given a key, return the value. if the key doesn't exist raise an error
        """
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]

        # since we have a linked list, lets traverse it
        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
        raise KeyError(f'key not found: {key}')


if __name__ == "__main__":
    ht_1 = HashTable()
    ht_1.set("name", "Adam")
    ht_1.set("age", "33")
    print(ht_1._buckets)
