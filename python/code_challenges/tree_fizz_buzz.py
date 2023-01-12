from data_structures.binary_tree import BinaryTree, Node
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue

# def fizz_buzz_tree(root):
#     if not root:
#         return None
#
#     if root.value % 3 == 0 and root.value % 5 == 0:
#         root.value = "FizzBuzz"
#     elif root.value % 3 == 0:
#         root.value = "Fizz"
#     elif root.value % 5 == 0:
#         root.value = "Buzz"
#     else:
#         root.value = str(root.value)
#
#     for child in root.children:
#         fizz_buzz_tree(child)
#
#     return root


# def fizz_buzz_tree(tree):
#
#     def helper(node):
#         if node.children:
#             for i in node.children:
#                 helper(i)
#         if node.value % 3 == 0 and node.value % 5 == 0:
#             node.value = 'FizzBuzz'
#         elif node.value % 3 == 0:
#             node.value = 'Fizz'
#         elif node.value % 5 == 0:
#             node.value = 'Buzz'
#         if node.children:
#             for i in node.children:
#                 helper(i)
#
#     helper(tree.root)
#
#     return tree

# def fizz_buzz_tree(tree):
#
#     def value_check(node):
#         """
#         checking nodes recursvely inorder: left, root, right
#         """
#         if node.left_child:
#             value_check(node.left_child)
#             # breakpoint()
#         if node.value % 3 == 0 and node.value % 5 == 0:
#             node.value = 'FizzBuzz'
#         elif node.value % 3 == 0:
#             node.value = 'Fizz'
#         elif node.value % 5 == 0:
#             node.value = 'Buzz'
#         if node.right_child:
#             value_check(node.right_child)
#     """
#     calling initial function on root of tree to start traversing
#     """
#     value_check(tree.root)
#     return tree
# def fizz_buzz_tree(tree):
#     def helper(node):
#         """
#         checking nodes recursvely inorder: left, root, right
#         """
#         if node.children:
#             breakpoint()
#             for i in node.children:
#                 helper(i)
#
#         if node.value % 3 == 0 and node.value % 5 == 0:
#             new_node = Node('FizzBuzz')
#             node.children.append(new_node)
#             node.value = new_node
#         elif node.value % 3 == 0:
#             new_node = Node('Fizz')
#             node.children.append(new_node)
#             node.value = new_node
#         elif node.value % 5 == 0:
#             new_node = Node('Buzz')
#             node.children.append(new_node)
#             node.value = new_node
#
#     helper(tree.root)
#     return tree

def fizz_buzz_tree(tree):
    fizzy_tree = tree.clone()

    if not tree.root:
        return fizzy_tree

    breadth = Queue()

    breadth.enqueue(fizzy_tree.root)

    while not breadth.is_empty():
        front = breadth.dequeue()
        front.value = fizzify(front.value)
        for child in front.children:
            breadth.enqueue(child)

    return fizzy_tree


def fizzify(num):
    txt = ""
    if num % 3 == 0:
        txt += "Fizz"
    if num % 5 == 0:
        txt += "Buzz"
    return txt or str(num)
