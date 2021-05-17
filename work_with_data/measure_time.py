from csv import writer
from os import mkdir, listdir
from time import time
from statistics import mean, median

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



DIR_PATH = "/home/bushmester/Desktop/dijkstra-algorithm/work_with_data/load_testing_data/"


def measute_time():
    file_with_testing_data = sorted(
        listdir(path=DIR_PATH)
        # listdir(path=DIR_PATH), key=lambda x: int(x[:-4])
    )

    size_do_have = set()
    result = []
    results = dict()

    with open(f"/home/bushmester/Desktop/dijkstra-algorithm/work_with_data/load_testing_mesurenets/{time()}.csv", "w") as file:
        creat_table = writer(file, delimiter=",")
        creat_table.writerow(
            ["size", "min", "max", "avg", "median"]
        )

        for test_file in file_with_testing_data:
            print(test_file)
            with open(DIR_PATH + f"{test_file}") as file:
                matrix = []
                size = int(file.readlines(1)[0][:-1])
                if size not in size_do_have:
                    results[size] = []

                for lines in file:
                    el = list(map(int, lines.split()))
                    matrix.append(el)

                start_node = matrix.pop(-1)[0]

                start = time()
                naive_dijkstra(matrix, start_node)
                end = time() - start

                if size in size_do_have:
                    result.clear()
                    result.append(end)
                    results[size] += result
                else:
                    size_do_have.add(size)
                    result.clear()
                    result.append(end)
                    results[size] += result

        for size in results:
            creat_table.writerow(
                [size, min(results[size]), max(results[size]),
                 mean(results[size]), median(results[size])]
            )


measute_time()
