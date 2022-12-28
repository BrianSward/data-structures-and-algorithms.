
from my_work.linked_list import LinkedList


# these are the tests i was asked to write, with little or no idea how to do tests
# or if i should even initialize this into a venv i have no clue what im doing and following instructions
# has proven DIFFICULT AF

# test 1
# Can successfully instantiate an empty linked list
def test_instantiate():
    assert LinkedList()


# test 2
# Can properly insert into the linked list

def test_insert():
    linked_list = LinkedList()
    linked_list.insert("horse")
    linked_list.insert("cow")
    expected = "cow"
    assert linked_list.insert("cow").value == expected

# test 3
# The head property will properly point to the first node in the linked list


def test_link_to_head():
    linked_list = LinkedList()
    linked_list.insert("cow")
    assert linked_list.head.value == "cow"


# test 4
# Can properly insert multiple nodes into the linked list
def test_insert_multiples():
    linked_list = LinkedList()
    expected_1 = linked_list.insert("horse")
    expected_2 = linked_list.insert("cow")
    assert linked_list.insert("horse").value == expected_1.value
    assert linked_list.insert("cow").value == expected_2.value

# test 5
# Will return true when finding a value within the linked list that exists


def test_includes_true():
    linked_list = LinkedList()
    linked_list.insert("horse")
    linked_list.insert("cow")
    assert linked_list.includes("horse")

# test 6
# Will return false when searching for a value in the linked list that does not exist


def test_includes_false():
    linked_list = LinkedList()
    linked_list.insert("horse")
    linked_list.insert("cow")
    assert not linked_list.includes("donkey")


# test 7
# Can properly return a collection of all the values that exist in the linked list
def test_to_string_double():
    linked_list = LinkedList()
    linked_list.insert("cow")
    assert print(linked_list) == "{ cow } -> NULL"
    linked_list.insert("horse")
    assert print(linked_list) == "{ horse } -> { cow } -> NULL"
