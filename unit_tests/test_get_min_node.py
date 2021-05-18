from naive_realization import get_min_node
import pytest


test_data = [
                ([0, 7, 3, 14], {1}, 0),
                ([7, 0, 4, 15], {0}, 1),
                ([4, 6, 0, 3, 8, 6], {5}, 2),
                ([2, 0, 6, 3, 8, 6], {2}, 1),
                ([5, 8, 5, 2, 4, 0], {1}, 5),
                ([3, 6, 4, 0, 6, 2], {4}, 3)
            ]

@pytest.mark.parametrize("shortest_paths, checked_vertex, expected_result", test_data)
def test_get_min_node(shortest_paths, checked_vertex, expected_result):
    assert get_min_node(shortest_paths, checked_vertex) == expected_result