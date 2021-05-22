from dijkstra_algorithm import __version__
import pytest
from dijkstra_algorithm.dijkstra_strategy import NaiveDijkstraAlgorithmStrategy, SetDijkstraAlgorithmStrategy


class TestDijkstraStrategy:
    test_data_for_naive = [(
            [[0, 3, 1, 3, 0, 0],
             [3, 0, 4, 0, 0, 0],
             [1, 4, 0, 0, 7, 5],
             [3, 0, 0, 0, 0, 2],
             [0, 0, 7, 0, 0, 4],
             [0, 0, 5, 2, 4, 0]], 3, [3, 6, 4, 0, 6, 2]),
        (
            [[0, 3, 1, 3, 0, 0],
             [3, 0, 4, 0, 0, 0],
             [1, 4, 0, 0, 7, 5],
             [3, 0, 0, 0, 0, 2],
             [0, 0, 7, 0, 0, 4],
             [0, 0, 5, 2, 4, 0]], 5, [5, 8, 5, 2, 4, 0]),
        (
            [[0, 2, 4, 8, 0, 16],
             [2, 0, 0, 3, 0, 0],
             [4, 0, 0, 3, 0, 0],
             [8, 3, 3, 0, 5, 3],
             [0, 0, 0, 5, 0, 5],
             [16, 0, 0, 3, 5, 0]], 1, [2, 0, 6, 3, 8, 6]),
        (
            [[0, 2, 4, 5, 10, 8],
             [2, 0, 0, 3, 0, 0],
             [4, 0, 0, 3, 0, 0],
             [8, 3, 3, 0, 5, 3],
             [0, 0, 0, 5, 0, 5],
             [16, 0, 0, 3, 5, 0]], 2, [4, 6, 0, 3, 8, 6]),
        (
            [[0, 10, 3, 0],
             [10, 0, 4, 0],
             [3, 4, 0, 11],
             [0, 0, 11, 0]], 1, [7, 0, 4, 15]),
        (
            [[0, 7, 3, 14],
             [10, 0, 4, 0],
             [3, 4, 0, 11],
             [0, 0, 11, 0]], 0, [0, 7, 3, 14])]

    test_false_data_for_naive = [
        (
            [[0, 7, 3, 14],
             [10, 0, 4, 0],
             [3, 4, 0, 11],
             [0, 0, 11, 0]], 0, [1, 2, 8, 14]),
        (
            [[0, 2, 4, 5, 10, 8],
             [2, 0, 0, 3, 0, 0],
             [4, 0, 0, 3, 0, 0],
             [8, 3, 3, 0, 5, 3],
             [0, 0, 0, 5, 0, 5],
             [16, 0, 0, 3, 5, 0]], 2, [2, 3, 0, 3, 5, 6])]

    test_data_for_set = [(
            [[0, 4, 2, 3, 0, 0],
             [1, 0, 4, 0, 0, 0],
             [1, 7, 0, 0, 8, 1],
             [7, 0, 0, 0, 0, 1],
             [0, 0, 2, 0, 0, 5],
             [0, 0, 3, 2, 2, 0]], 2, [1, 5, 0, 3, 3, 1]),
        (
            [[0, 6, 2, 8, 0, 0],
             [1, 0, 8, 0, 7, 0],
             [5, 7, 0, 0, 7, 5],
             [6, 2, 0, 0, 0, 9],
             [1, 0, 4, 0, 0, 2],
             [0, 0, 2, 2, 4, 0]], 5, [5, 4, 2, 2, 4, 0]),
        (
            [[0, 2, 4, 8, 0, 16],
             [2, 0, 0, 3, 0, 0],
             [11, 0, 0, 2, 11, 0],
             [8, 2, 3, 0, 11, 3],
             [0, 0, 14, 2, 0, 9],
             [16, 0, 2, 3, 5, 0]], 1, [2, 0, 6, 3, 11, 6]),
        (
            [[0, 13, 4, 5, 10, 8],
             [11, 0, 12, 7, 0, 7],
             [13, 0, 0, 2, 0, 0],
             [1, 1, 1, 0, 1, 3],
             [0, 2, 0, 8, 0, 3],
             [12, 2, 8, 3, 5, 0]], 2, [3, 3, 0, 2, 3, 5]),
        (
            [[0, 1, 13, 0],
             [8, 0, 7, 2],
             [1, 7, 0, 12],
             [0, 1, 1, 0]], 1, [4, 0, 3, 2]),
        (
            [[0, 4, 2, 4],
             [1, 0, 4, 1],
             [3, 4, 0, 11],
             [12, 0, 11, 0]], 0, [0, 4, 2, 4])]

    test_false_data_for_set = [
        (
            [[0, 1, 1, 24],
             [11, 0, 14, 12],
             [24, 11, 0, 1],
             [12, 8, 1, 0]], 1, [1, 2, 8, 14]),
        (
            [[0, 2, 6, 6, 6, 6],
             [12, 0, 3, 23, 13, 16],
             [12, 11, 0, 3, 5, 8],
             [9, 9, 9, 0, 1, 2],
             [3, 4, 5, 13, 0, 8],
             [1, 2, 3, 6, 9, 0]], 2, [2, 3, 0, 3, 5, 6])]

    @pytest.mark.parametrize("matrix, vertex, expected_result", test_data_for_naive)
    def test_naive_dijkstra_algorithm_strategy(self, matrix, vertex, expected_result):
        naive_dijkstra = NaiveDijkstraAlgorithmStrategy()
        assert naive_dijkstra.search_shortest_path(matrix, vertex) == expected_result

    @pytest.mark.parametrize("matrix, vertex, expected_result", test_false_data_for_naive)
    def test_false_naive_dijkstra_algorithm_strategy(self, matrix, vertex, expected_result):
        naive_dijkstra = NaiveDijkstraAlgorithmStrategy()
        assert naive_dijkstra.search_shortest_path(matrix, vertex) != expected_result

    @pytest.mark.parametrize("matrix, vertex, expected_result", test_data_for_set)
    def test_set_dijkstra_algorithm_strategy(self, matrix, vertex, expected_result):
        set_dijkstra = SetDijkstraAlgorithmStrategy()
        assert set_dijkstra.search_shortest_path(matrix, vertex) == expected_result

    @pytest.mark.parametrize("matrix, vertex, expected_result", test_false_data_for_set)
    def test_false_set_dijkstra_algorithm_strategy(self, matrix, vertex, expected_result):
        set_dijkstra = SetDijkstraAlgorithmStrategy()
        assert set_dijkstra.search_shortest_path(matrix, vertex) != expected_result


def test_version():
    assert __version__ == '0.1.0'
