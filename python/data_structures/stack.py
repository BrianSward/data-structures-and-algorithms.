from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    class for a stack
    """

    def __init__(self):
        self.top = None

    def push(self, cosita):
        """
        takes in a cosita and places it on top of the stack
        """
        if self.top is None:
            self.top = Node(cosita)
            return
        dummy = self.top
        self.top = Node(cosita)
        self.top.next = dummy

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        popped = self.top
        self.top = self.top.next
        return popped.value

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
