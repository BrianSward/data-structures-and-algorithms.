# Challenge Summary
<!-- Description of the challenge -->
Problem Domain:
Write the following method for the Graph class:

Name: Depth first
Arguments: Node (Starting point of search)
Return: A collection of nodes in their pre-order depth-first traversal order
Program output: Display the collection

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](whiteboard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Approach:
recursive dfs
### Space and Time:
SPACE: O(n) for n being the scaling nature of a graph as it grows in size
TIME: O( edges + nodes ) for the number of edges and nodes in our graph which i think reduces to O(n) ultimately
## Solution
<!-- Show how to run your code, and examples of it in action -->

just `pytest teat/test_graph_depth_first.py`
