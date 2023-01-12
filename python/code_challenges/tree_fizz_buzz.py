from data_structures.binary_tree import BinaryTree, Node
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def fizz_buzz_tree(tree):
    
    cloned = tree.clone()
    def helper(node):
        if node.children:
            for i in node.children:
                helper(i)
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'FizzBuzz'
        elif node.value % 3 == 0:
            node.value = 'Fizz'
        elif node.value % 5 == 0:
            node.value = 'Buzz'
        else:
            node.value = str(node.value) # jb: convert numbers to strings

        # jb: remove this bit
        # if node.children:
        #     for i in node.children:
        #         helper(i)

    helper(cloned.root)
    return cloned
