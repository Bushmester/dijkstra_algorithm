import math


def get_min_node(shortest_paths, checked_vertex):
    vertex = False
    max_weight = max(shortest_paths)

    for idx_vtx, weight in enumerate(shortest_paths):

        if weight < max_weight and idx_vtx not in checked_vertex:
            max_weight = weight
            vertex = idx_vtx

    return vertex


def naive_dijkstra(matrix, vertex):
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


def main():
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

    """
    Input:


    nodes_count = int(input())
    matrix = [list(map(int, input().split())) for i in range(nodes_count)]
    start_node = int(input())
    while start_node >= nodes_count:
        start_node = int(input())
    """

    # print(naive_dijkstra(matrix, 0))


if __name__ == '__main__':
    main()
