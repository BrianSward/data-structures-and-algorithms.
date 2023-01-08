from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    # had trouble getting recursion working, had to do it with iterations

    # def add(self, value):
    #     test = Node(value)
    #     if self.root is None:
    #         self.root = test
    #         return
    #     if self.root.value < test.value:
    #         if test.left is None:
    #             test.left = Node(value)
    #         else:
    #             self.add(value, test.left)
    #
    #     elif self.root.value > test.value:
    #         if test.right is None:
    #             test.right = Node(value)
    #         else:
    #             self.add(value, test.right)

    # had help with this from a ta as we talked through code

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        prev = None
        temp = self.root
        while temp is not None:
            if temp.value > value:
                prev = temp
                temp = temp.left
            elif temp.value < value:
                prev = temp
                temp = temp.right
        if prev.value > value:
            prev.left = node
        else:
            prev.right = node


    def contains(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False


