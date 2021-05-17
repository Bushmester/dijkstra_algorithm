from csv import writer
from os import mkdir, listdir
from time import time
from statistics import mean, median


DIR_PATH = "/home/bushmester/study/study_programming/cpp/dijkstra-algorithm/work_with_data/load_testing_data/"


def measute_time():
    file_with_testing_data = sorted(
        listdir(path=DIR_PATH), key=lambda x: int(x[:-4])
    )

    size_do_have = set()
    result = []
    results = dict()

    with open(f"load_testing_mesurenets/{time()}.csv", "w") as file:
        creat_table = writer(file, delimiter=",")
        creat_table.writerow(
            ["size", "min", "max", "avg", "median"]
        )

        for test_file in file_with_testing_data:
            with open(DIR_PATH + f"{test_file}") as file:
                matrix = []
                size = int(file.readlines(1)[0][:-1])
                results[size] = []

                for lines in file:
                    el = list(map(int, lines.split()))
                    matrix.append(el)

                start_node = matrix.pop(-1)[0]

                start = time()
                # naive_dijkstra(matrix, start_node)
                end = time() - start

                if size in size_do_have:
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
