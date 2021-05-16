from random import randint
from math import inf
from os import mkdir
import time

from multiprocessing import Pool


DIR_PATH = "/home/bushmester/study/study_programming/cpp/dijkstra-algorithm/dijkstra_algorithm/work_with_data/load_testing_data_naiv/"


def create_itarable_with_combination(start: int, end: int, step: int, count: int) -> list:  
    for i in range(start, end, step):
        for j in range(1, count + 1):
            yield i, j


def create_adjacency_matrix(size: int, number: int):
    with open(DIR_PATH + f"{size}_{number}.txt", "w") as file:
        count_of_nodes = size
        random_number = randint(1, 2 ** 10)
        adjacency_matrix = [
            [inf for _ in range(count_of_nodes)] for _ in range(count_of_nodes)
        ]

        for _ in range(random_number):
            random_first_index = randint(1, count_of_nodes)
            random_second_index = randint(1, count_of_nodes)
            weight = randint(1, random_number)
            adjacency_matrix[
                random_first_index - 1
            ][
                random_second_index - 1
            ] = weight

        for index in range(count_of_nodes):
            adjacency_matrix[index][index] = 0

        file.write(str(adjacency_matrix))


def generate_data(start: int, end: int, step: int, count: int):
    with Pool() as pool:
        pool.starmap(
            create_adjacency_matrix,
            list(create_itarable_with_combination(
                start, end, step, count
            ))
        )


def main():
    try:
        mkdir(DIR_PATH)
    except:
        pass
    
    start = time.time()
    generate_data(
        start=2,
        end=100,
        step=1,
        count=100
    )
    print(time.time() - start)


if __name__ == "__main__":
    main()
