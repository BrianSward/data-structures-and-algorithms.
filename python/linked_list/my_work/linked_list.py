class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """you can add a new node which will replace your current head"""
        a = Node(value)
        a.next = self.head
        self.head = a

    def includes(self, value):
        """will check linkedlist for the value given"""
        startat = self.head
        init = True
        while startat != None:
            if startat.value == value:
                return init
            startat = startat.next
        init = False
        return init

    def __str__(self):
        """returns a string of what is inside our linked list with proper formatting"""
        target = []
        spoint = self.head
        return_me = ""

        while spoint:
            target.append(spoint.value)
            spoint = spoint.next
        for x in target:
            return_me += f"{{ {x} }} -> "
        return_me += "NULL"
        return return_me


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
