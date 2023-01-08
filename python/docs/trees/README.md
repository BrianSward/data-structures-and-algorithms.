# Trees
<!-- Short summary or background information -->
In this assignment, we’ll be covering Binary Trees, and Binary Search Trees.  We cover methods which will be
outlined below.

Common Terminology:
- Node - A Tree node is a component which may contain its own values, and references to other nodes
- Root - The root is the node at the beginning of the tree
- K - A number that specifies the maximum number of children any node may have in a k-ary tree. In a binary tree, k = 2.
- Left - A reference to one child node, in a binary tree
- Right - A reference to the other child node, in a binary tree
- Edge - The edge in a tree is the link between a parent and child node
- Leaf - A leaf is a node that does not have any children
- Height - The height of a tree is the number of edges from the root to the furthest leaf

## Challenge
<!-- Description of the challenge -->
- Create Node, Binary Tree, Binary Search Tree classes (and subclasses as app.) and methods contains, add, and a
a variety of methods outlined below

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I took a recursive approach to contains, and a step through method for add. I believe the orders in the Binary Tree is is time O(N) and the space is O(1).
For add i think it is Log(N) for adding as you have to go through a lot but not everything
For contains again i think it is Log(N) for contains as you have to go through a bunch but not all things.

## API
<!-- Description of each method publicly available in each of your trees -->

### Binary Tree Methods

- BinaryTree.post_order: Will return a list of nodes in left, right, root order
- BinaryTree.pre_order Will return a list of nodes in root, left, right order
- BinaryTree.in_order Will return a list of nodes in left, root, right order

### Binary Search Tree Methods

- BinarySearchTree.add: Adds a new node with that value in the correct location in the binary search tree.
- BinarySearchTree.contains: Returns a boolean indicating if the value is in the tree at least once.
