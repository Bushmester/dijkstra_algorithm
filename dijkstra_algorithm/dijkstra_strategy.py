from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

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

    def search_shortest_path(self, matrix: List[List], vertex: int) -> List:
        return self._dijkstra_algorithm.search_shortest_path(matrix, vertex)


class DijkstraAlgorithmStrategy(ABC):
    @abstractmethod
    def search_shortest_path(self, matrix: List[List], vertex: int) -> List:
        pass


class NaiveDijkstraAlgorithmStrategy(DijkstraAlgorithmStrategy):
    def search_shortest_path(self, matrix: List[List], vertex: int) -> List:
        return naive_dijkstra()


class SetDijkstraAlgorithmStrategy(DijkstraAlgorithmStrategy):
    def search_shortest_path(self, matrix: List[List], vertex: int) -> List:
        return set_dijkstra()
