from random import randint
from math import inf
import time

from multiprocessing import Pool


def generate_data(start: int, end: int, step: int, count: int, dir_path: str):
    for i in range(start, end, step):
        for j in range(1, count + 1):
            with open(dir_path + f"{i}_{j}.txt", "w") as file:
                count_of_nodes = i
                count_of_edges = randint(start, end * 2 ** 5)
                adjacency_matrix = [
                    [inf for _ in range(count_of_nodes)] for _ in range(count_of_nodes)
                ]

                for _ in range(count_of_edges):
                    first_node = randint(1, count_of_nodes)
                    second_node = randint(1, count_of_nodes)
                    weight = randint(start, end ** 2 ** 5)
                    adjacency_matrix[first_node - 1][second_node - 1] = weight

                for index in range(count_of_nodes):
                    adjacency_matrix[index][index] = 0

                file.write(str(adjacency_matrix))


def multi_generate_data(start: int, end: int, step: int, count: int, dir_path: str):
    with Pool() as pool:
        pool.apply_async(generate_data(start, end, step, count, dir_path))
