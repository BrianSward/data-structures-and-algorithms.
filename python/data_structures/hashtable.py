class Node:
    """
    for use with the Linked List below
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    for use with the HashTable below
    """

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

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def insert(self, item):
        """
        provided by raven as a part of the code jb used to make tests
        :param item:
        :return:
        """
        node = Node(item)
        # if list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node


class Hashtable:
    """
    Implementation of a Hashtable Class with the following methods:
        set, get, has, keys, hash
    """

    def __init__(self, size=10):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        """
        Takes in a key and will assign a hash number to it, an integer is returned representing the index of its location in the list
        :param key:
        :return: Index in the collection for that key
        """
        hash__ = 0
        for char in key:
            hash__ += ord(char)
        # hash represents index of bucket in hash table
        hash__ = (hash__ * 19) % self.size
        return hash__

    def set(self, key, value):
        """
        this method puts items into the hashtable for us
        :param key: key for the key value pair
        :param value: value for the key value pair
        :return:
        """
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        if not bucket:
            self._buckets[hashed_key] = LinkedList()
        self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        """
        this method will return a value inside a hashtable associated to a key
        :param key: key value you're looking to find values at
        :return: will return the value at the key in the hashtable
        """
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        if not bucket:
            return None
        # since we have a linked list, lets traverse it
        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
        return None

    def has(self, key):
        """
        will check the hashtable to see if the key already exists in it. based on its presence return boolean
        :param key: the value you're looking for inside the hashtable
        :return: true/false
        """
        hashed_key = self._hash(key)
        if not self._buckets[hashed_key]:
            return False
        bucket = self._buckets[hashed_key].head
        while bucket:
            if bucket.value[0] == key:
                return True
            bucket = bucket.next
        return False

    def keys(self):
        """
        this method will return a list of keys inside our hashtable
        :return: a list of keys
        """
        keys = []
        for key in self._buckets:
            if key is not None:
                keys.append(key.head.value[0])
        return keys


if __name__ == "__main__":
    hashtable = Hashtable()
    hashtable.set("name", "brian")
    hashtable.set("name", "running")
    print(hashtable._buckets)
    print(hashtable.get('name'))
