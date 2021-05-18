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


# class SetDijkstraAlgorithmStrategy(DijkstraAlgorithmStrategy):
#     def search_shortest_path(self, matrix: List[List], vertex: int) -> List[int]:
#         return set_dijkstra()


"""
    Test matrix


    matrix = [[0, 3, 1, 3, 0, 0],       # [0, 3, 1, 3, 8, 5]
              [3, 0, 4, 0, 0, 0],
              [1, 4, 0, 0, 7, 5],
              [3, 0, 0, 0, 0, 2],
              [0, 0, 7, 0, 0, 4],
              [0, 0, 5, 2, 4, 0]]

    matrix = [[0, 2, 4, 8, 0, 16],      # [0, 2, 4, 5, 10, 8]
              [2, 0, 0, 3, 0, 0],
              [4, 0, 0, 3, 0, 0],
              [8, 3, 3, 0, 5, 3],
              [0, 0, 0, 5, 0, 5],
              [16, 0, 0, 3, 5, 0]]

    matrix = [[0, 10, 3, 0],            # [0, 7, 3, 14]
              [10, 0, 4, 0],
              [3, 4, 0, 11],
              [0, 0, 11, 0]]
    """
