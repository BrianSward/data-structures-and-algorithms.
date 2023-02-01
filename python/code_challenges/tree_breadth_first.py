from python.data_structures.binary_tree import BinaryTree, Node


def breadth_first(tree):
    if not tree.root:
        return []

    stack = [tree.root]
    nodes = []

    while stack:
        node = stack.pop()
        nodes.append(node.value)
        if node.left:
            stack.insert(0, node.left)
        if node.right:
            stack.insert(0, node.right)

    return nodes
