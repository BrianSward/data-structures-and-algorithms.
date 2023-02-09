try:
    from python.data_structures.invalid_operation_error import InvalidOperationError
except:
    from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    data structure with idea of its front and rear
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        # jb: refactored to fix hard to find bug
        # jb: tried to keep it as close as possible to old
        new_node = Node(val)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = self.rear.next

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def dequeue(self):
        try:
            dequeued = self.front
            self.front = self.front.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        if self.front is None:
            return True

