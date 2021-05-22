from multiprocessing import Pool
from random import randint
import sys

from dijkstra_algorithm.config import TESTING_DATA


def create_itarable_with_combination(start: int, end: int, step: int, count: int) -> list:
    for i in range(start, end, step):
        for j in range(1, count + 1):
            yield i, j


def create_adjacency_matrix(size: int, number: int):
    with open(TESTING_DATA + f"{size}_{number}.txt", "w") as file:
        file.write(str(size) + "\n")
        adjacency_matrix = [[randint(0, sys.maxsize) for i in range(size)] for j in range(size)]

        for i in range(size):
            adjacency_matrix[i][i] = 0

        for i in range(size):
            for j in range(size):
                will_be_num = randint(0, 10)
                if not will_be_num:
                    adjacency_matrix[i][j] = 0
                adjacency_matrix[j][i] = adjacency_matrix[i][j]

        for elements in range(size):
            for element in range(len(adjacency_matrix[elements])):
                separ = " "
                if element == len(adjacency_matrix[elements]) - 1:
                    separ = "\n"
                file.write(str(adjacency_matrix[elements][element]) + separ)

        file.write(str(randint(0, size - 1)))


def generate_data_func(start: int, end: int, step: int, count: int):
    with Pool() as pool:
        pool.starmap(
            create_adjacency_matrix,
            list(create_itarable_with_combination(
                start, end, step, count
            ))
        )
