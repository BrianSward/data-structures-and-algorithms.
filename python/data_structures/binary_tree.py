class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def post_order(self, root=None, nodes=None):
        """
        return a list of nodes in a binary tree in post order
        given below, return [4, 5, 2, 6, 7, 3, 1]
        """

        # method
        # initially start at root
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        # left child
        if root.left:
            self.post_order(root.left, nodes)
        # right child
        if root.right:
            self.post_order(root.right, nodes)
        # root
        nodes.append(root.value)

        return nodes

    def pre_order(self, root=None, nodes=None):
        """
        return a list of nodes in a binary tree in pre order
        given below, return [1, 2, 4, 5, 3, 6, 7]
        """
        # method
        # initially start at root
        if root is None:
            root = self.root
        # root
        if nodes is None:
            nodes = []

        nodes.append(root.value)

        # left child
        if root.left:
            self.pre_order(root.left, nodes)
        # right child
        if root.right:
            self.pre_order(root.right, nodes)

        return nodes

    def in_order(self, root=None, nodes=None):
        """
        return a list of nodes in a binary tree in order
        given below, return [4, 2, 5, 1, 6, 3, 7]
        """
        # method
        # initially start at root
        if root is None:
            root = self.root
        if nodes is None:
            nodes = []
        # left child
        if root.left:
            self.in_order(root.left, nodes)

        # root
        nodes.append(root.value)

        # right child
        if root.right:
            self.in_order(root.right, nodes)

        return nodes


if __name__ == "__main__":
    """
            1
          /   \
         2     3
        / \   / \
       4   5 6   7
    """
    bt_1 = BinaryTree()
    bt_1.root = Node(1)
    bt_1.root.left = Node(2)
    bt_1.root.right = Node(3)
    bt_1.root.left.left = Node(4)
    bt_1.root.left.right = Node(5)
    bt_1.root.right.left = Node(6)
    bt_1.root.right.right = Node(7)
    print("post order: ", bt_1.post_order())
    print("")
    print("pre order: ", bt_1.pre_order())
    print("")
    print("in order: ", bt_1.in_order())
