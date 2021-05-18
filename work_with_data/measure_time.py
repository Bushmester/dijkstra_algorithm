from csv import writer
from os import mkdir, listdir
from time import time
from statistics import mean, median

from .. import config 


def measute_time(func):
    file_with_testing_data = sorted(
        listdir(path=config.TESTING_DATA)
    )

    size_do_have = set()
    result = []
    results = dict()

    with open(config.MEASUREMENTS + str(time()) + ".csv", "w") as file:
        creat_table = writer(file, delimiter=",")
        creat_table.writerow(
            ["size", "min", "max", "avg", "median"]
        )

        for test_file in file_with_testing_data:
            print(test_file)
            with open(config.TESTING_DATA + str(test_file)) as file:
                matrix = []
                size = int(file.readlines(1)[0][:-1])
                if size not in size_do_have:
                    results[size] = []

                for lines in file:
                    el = list(map(int, lines.split()))
                    matrix.append(el)

                start_node = matrix.pop(-1)[0]

                start = time()
                func(matrix, start_node)
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
