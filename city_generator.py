from itertools import pairwise
from random import choice, uniform

from networkx import Graph, barabasi_albert_graph

NEW_NODE_EDGES = 3
BUS_STOPS = 10


def random_path(graph: Graph, max_len):
    path = [choice(list(graph.nodes()))]

    for _ in range(max_len):
        candidates = list(
            neighbor for neighbor in graph.neighbors(path[-1]) if neighbor not in path
        )

        if candidates:
            path.append(choice(candidates))
        else:
            break

    return path


BUS_LINE_KEY = "bus_line"
EDGE_LENGTH_LIMITS = (10, 100)


def generate_city_graph(nodes=100, bus_lines=10):
    graph: Graph = barabasi_albert_graph(nodes, NEW_NODE_EDGES)

    for edge in graph.edges():
        graph[edge[0]][edge[1]]["length"] = uniform(*EDGE_LENGTH_LIMITS)

    for bus_line in range(bus_lines):
        for i, j in pairwise(random_path(graph, BUS_STOPS)):
            edge = graph[i][j]

            if BUS_LINE_KEY in edge:
                edge[BUS_LINE_KEY].append(bus_line)
            else:
                edge[BUS_LINE_KEY] = [bus_line]

    return graph
