from multiprocessing import Pool
from random import randint

DIR_PATH = "/home/bushmester/study/study_programming/cpp/dijkstra-algorithm/work_with_data/load_testing_data/"


def create_itarable_with_combination(start: int, end: int, step: int, count: int) -> list:
    for i in range(start, end, step):
        for j in range(1, count + 1):
            yield i, j


def create_adjacency_matrix(size: int, number: int):
    with open(DIR_PATH + f"{size}_{number}.txt", "w") as file:
        file.write(str(size) + "\n")
        count_of_nodes = size
        random_number = randint(1, 2 ** 10)
        adjacency_matrix = [
            [-1 for _ in range(count_of_nodes)] for _ in range(count_of_nodes)
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

        for elements in range(size):
            for element in range(len(adjacency_matrix[elements])):
                separ = " "
                if element == len(adjacency_matrix[elements]) - 1:
                    separ = "\n"
                file.write(str(adjacency_matrix[elements][element]) + separ)


def generate_data(start: int, end: int, step: int, count: int):
    with Pool() as pool:
        pool.starmap(
            create_adjacency_matrix,
            list(create_itarable_with_combination(
                start, end, step, count
            ))
        )
