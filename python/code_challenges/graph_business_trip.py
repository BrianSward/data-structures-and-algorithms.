try:
    from python.data_structures.graph import Graph
except:
    from data_structures.graph import Graph


def direct_flights(planets, names):
    """
    takes in graph of planets and a list of names
    :param planets: a graph
    :param names: a list of places to see if direct flights exist between
    :return: True and the cost or False and 0
    """

    # a list to keep track of where I have been
    visited = set()
    # let see all the places we may want to go
    nodes = planets.get_nodes()
    # recursive way

    def dfs(node, target, cost):
        """
        recursive depth first search to see if our planet can see the other planet (is there a link)
        :param node: the location we are starting at
        :param target: our destination node
        :param cost: the current cost of the trip (used for the recursive call)
        :return: true and the cost if it exists or false and 0 if it doesn't
        """
        # covering base cases // stops our recursion
        if node == target:
            return True, cost
        # add where we started to the dictionary

        visited.add(node)
        # get all the n'bors of where we start
        for _edge in planets.get_neighbors(node):
            # if we haven't been there
            if _edge.vertex not in visited:
                # look at next node, see if path exists
                if dfs(_edge.vertex, target, cost + _edge.weight) is not None:
                    is_path, path_cost = dfs(_edge.vertex, target, cost + _edge.weight)
                # if out path exists return true/cost
                if is_path:
                    return True, path_cost
        return False, 0

    # **** WHERE I AM STRUGGLING ****

    for node_ in nodes:
        for name in names:
            dfs(node_, name, 0)

    # # non-recursive way this checks for direct flights
    # if len(names) == 2:
    #     # make nodes that we can compare if they are n'bors
    #     node_1 = [node for node in nodes if node.value == names[0]][0]
    #     node_2 = [node for node in nodes if node.value == names[1]][0]
    #     # now we match
    #     for __edge in planets.get_neighbors(node_1):
    #         if __edge.vertex == node_2:
    #             # if the node matches a value in the list
    #             return True, __edge.weight
    #     # no matches, return false and zero
    #     return False, 0
    # # this checks for flights which have layovers, does the same as above but with three nodes
    # elif len(names) > 2:
    #     node_1 = [node for node in nodes if node.value == names[0]][0]
    #     node_2 = [node for node in nodes if node.value == names[1]][0]
    #     node_3 = [node for node in nodes if node.value == names[2]][0]
    #     # not happy with this, wonder if there is an easier way then nested if's
    #     for edge_1 in planets.get_neighbors(node_1):
    #         # here we compare and match
    #         if edge_1.vertex == node_2:
    #             # if we match we try the loop again
    #             for edge_2 in planets.get_neighbors(node_2):
    #                 if edge_2.vertex == node_3:
    #                     # if it makes it through second loop we're good
    #                     return True, edge_1.weight + edge_2.weight
    #     return False, 0


if __name__ == "__main__":
    graph = Graph()

    metroville = graph.add_node("Metroville")
    pandora = graph.add_node("Pandora")
    arendelle = graph.add_node("Arendelle")
    new_monstropolis = graph.add_node("New Monstropolis")
    naboo = graph.add_node("Naboo")
    narnia = graph.add_node("Narnia")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, pandora, 150)

    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, pandora, 82)

    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(arendelle, metroville, 99)

    graph.add_edge(new_monstropolis, arendelle, 42)
    graph.add_edge(arendelle, new_monstropolis, 42)

    graph.add_edge(new_monstropolis, metroville, 105)
    graph.add_edge(metroville, new_monstropolis, 105)

    graph.add_edge(new_monstropolis, naboo, 73)
    graph.add_edge(naboo, new_monstropolis, 73)

    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, metroville, 26)

    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(narnia, metroville, 37)

    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(naboo, narnia, 250)
    names__ = ["Arendelle", "New Monstropolis", "Naboo"]
    print(direct_flights(graph, names__))
