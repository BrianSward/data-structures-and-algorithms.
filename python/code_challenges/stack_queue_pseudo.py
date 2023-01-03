from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        if self.outbox.is_empty:
            while not self.inbox.is_empty:
                self.outbox.push(self.inbox.pop())
            return_me = self.outbox.pop()
            while not self.outbox.is_empty:
                self.inbox.push(self.outbox.pop())
        return return_me
