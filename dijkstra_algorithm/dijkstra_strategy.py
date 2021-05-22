from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

import math

from dijkstra_algorithm.functions.get_min_node import get_min_node


class UseDijkstraAlgorithm():
    def __init__(self, dijkstra_algorithm: DijkstraAlgorithmStrategy) -> None:
        self._dijkstra_algorithm = dijkstra_algorithm

    @property
    def dijkstra_algorithm(self) -> DijkstraAlgorithmStrategy:
        return self._dijkstra_algorithm

    @dijkstra_algorithm.setter
    def dijkstra_algorithm(self, dijkstra_algorithm: DijkstraAlgorithmStrategy) -> None:
        self._dijkstra_algorithm = dijkstra_algorithm

    def search_shortest_path(self, matrix: List[List], vertex: int) -> List[int]:
        return self._dijkstra_algorithm.search_shortest_path(matrix, vertex)


class DijkstraAlgorithmStrategy(ABC):
    @abstractmethod
    def search_shortest_path(self, matrix: List[List], vertex: int) -> List[int]:
        pass


class NaiveDijkstraAlgorithmStrategy(DijkstraAlgorithmStrategy):
    def search_shortest_path(self, matrix: List[List], vertex: int) -> List[int]:
        shortest_paths = [math.inf] * len(matrix)
        shortest_paths[vertex] = 0
        checked_vertex = {vertex}

        while vertex is not False:

            for i, weight in enumerate(matrix[vertex]):

                if i not in checked_vertex and weight != 0:
                    set_weight = shortest_paths[vertex] + weight

                    if set_weight < shortest_paths[i]:
                        shortest_paths[i] = set_weight

            vertex = get_min_node(shortest_paths, checked_vertex)

            if vertex is not False:
                checked_vertex.add(vertex)

        return shortest_paths


class SetDijkstraAlgorithmStrategy(DijkstraAlgorithmStrategy):
    def search_shortest_path(self, matrix: List[List], vertex: int) -> List[int]:
        soon = "soon"
        return soon
        # return set_dijkstra()
