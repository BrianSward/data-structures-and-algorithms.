try:
    from python.data_structures.binary_tree import BinaryTree, Node
    from python.data_structures.queue import Queue
except:
    from data_structures.binary_tree import BinaryTree, Node
    from data_structures.queue import Queue


def tree_intersection(t_one, t_two):
    po_t_one = t_one.post_order()
    po_t_two = t_two.post_order()
    value_dict = {
        "tree_one": po_t_one,
        "tree_two": po_t_two,
    }
    return_me = set()
    for i in value_dict["tree_one"]:
        if i in value_dict["tree_two"]:
            return_me.add(i)
    return return_me


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)


if __name__ == "__main__":
    tree_a = BinaryTree()
    values = [3, 4]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [4, 1, 3, 5, 6, 7, 9]
    add_values_to_empty_tree(tree_b, values)

    print(tree_intersection(tree_a, tree_b))
