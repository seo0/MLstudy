

import networkx as nx
import matplotlib.pyplot as plt

from module13_graphs01.part01_basics.graphs_basics import print_graph, display_and_save





def modulo_digraph(N,M):
    """
    This function returns a directed graph DiGraph) with the following properties (see also cheatsheet at: http://screencast.com/t/oF8Nr1TdYDbl):
    - The graph has N nodes, labelled using numbers from 1 to N-1
    - All nodes in the same M-modulo class are on the same path (the path from the node with lower value to highest value)
    - All nodes that are multiple of M-1 (or, in other words, for which node % (M-1) == 0) are on the same path (that gos from lower to higher values)

    Hint:
    - Initialise the DiGraph, for each node you can store two properties (value of % M, value of % (M-1))
    - Scan the created graph to create paths based on similar values of the two properties
    - Create edges in the graph using the values of the lists of nodes that you created at the previous step

    More about DiGraphs at: https://networkx.github.io/documentation/development/reference/classes.digraph.html
    """
    pass



def longest_shortest_path(G):
    """
    Given a graph G, this functions prints on screen the longest among the shortest paths between two nodes in G.
    note that you can check whether a path exists between two nodes using nx.has_path(G, node1, node2)
    If there are more than 1 longest shortest path, then it doesn't matter which one is chosen
    """
    pass

if __name__ == '__main__':
    G = modulo_digraph(6,3)
    print_graph(G)
    longest_shortest_path(G)
    G = modulo_digraph(7, 2)
    print_graph(G)
    G = modulo_digraph(10, 5)
    print_graph(G)
    longest_shortest_path(G)