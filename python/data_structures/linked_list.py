class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """you can add a new node which will replace your current head"""
        a = Node(value)
        a.next = self.head
        self.head = a

    def append(self, value):
        """adds a new node with the given value to the end of the list"""
        a = Node(value)
        while self.head == None:
            self.head = a
            return
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = a

    def insert_before(self, value, new_value):
        """adds a new node with the given new value immediately before the first node that has the value specified"""
        if self.head is None:
            raise TargetError()

        if not self.includes(value):
            raise TargetError()
        a = Node(new_value)

        if not self.head:
            self.head = a

        else:
            current = self.head
            if current.value == value:
                a.next = current
                self.head = a
            while current.next:
                if current.next.value == value:
                    a.next = current.next
                    current.next = a
                    break
                else:
                    current = current.next


    def insert_after(self, value, new_value):
        """adds a new node with the given new value immediately after the first node that has the value specified"""
        if self.head is None:
            raise TargetError()

        if not self.includes(value):
            raise TargetError()
        a = Node(new_value)
        if not self.head:
            self.head = a
        else:
            current = self.head
            while current:
                if current.value == value:
                    a.next = current.next
                    current.next = a
                    return
                else:
                    current = current.next




    def includes(self, value):
        """will check linkedlist for the value given"""
        startat = self.head
        init = True
        while startat:
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


class TargetError(Exception):
    pass
    # def __init__(self, message):
    #     self.message = message


