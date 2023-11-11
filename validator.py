from dataclasses import dataclass
from itertools import pairwise
from typing import Any, Callable, Dict

from networkx.classes.multidigraph import MultiDiGraph


@dataclass
class Problem:
    city_graph: MultiDiGraph
    start: int
    end: int
    edge_type_speed: Callable[[Any], int]


def validate_and_calculate(problem: Problem, route: list[int]):
    assert route[0] == problem.start
    assert route[-1] == problem.end

    time_distance = 0
    for i, j in pairwise(route):
        assert problem.city_graph.has_edge(i, j)
        edge_data = problem.city_graph.get_edge_data(i, j)
        time_distance += edge_data["length"] / problem.edge_type_speed(edge_data)

    return time_distance
