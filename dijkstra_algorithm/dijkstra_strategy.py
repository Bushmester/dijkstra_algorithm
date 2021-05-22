from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

import heapq
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
        ver_count = len(matrix)
        dist = [math.inf] * ver_count
        dist[vertex] = 0
        visited = set()
        pq = [(0, vertex)]

        while len(pq) != 0:
            current_len, ver = heapq.heappop(pq)

            if current_len > dist[ver] or ver in visited:
                continue

            for i in range(ver_count):
                to_ver = i
                current_len = matrix[ver][to_ver]

                if dist[to_ver] > current_len + dist[ver] and current_len > 0:
                    dist[to_ver] = current_len + dist[ver]
                    heapq.heappush(pq, (dist[to_ver], to_ver))

            visited.add(ver)

        return dist

