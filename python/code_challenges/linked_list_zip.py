
def zip_lists(a, b):

    if a is None:
        return b
    if b is None:
        return a

    a_current = a.head
    b_current = b.head

    while a_current and b_current:
        a_next = a_current.next
        b_next = b_current.next
        a_current.next = b_current
        if a_next:
            b_current.next = a_next
        a_current = a_next
        b_current = b_next

    if a.head:
        return a
    else:
        return b

