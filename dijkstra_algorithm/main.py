import click

from typing import List

from dijkstra_algorithm.dijkstra_strategy import UseDijkstraAlgorithm, NaiveDijkstraAlgorithmStrategy
# , SetDijkstraAlgorithmStrategy
from dijkstra_algorithm.functions.make_matrix import make_matrix
from dijkstra_algorithm.work_with_data.generate_data import generate_data_func
from dijkstra_algorithm.work_with_data.measure_time import measute_time_func
from dijkstra_algorithm.work_with_data.create_chart import create_chart_func


cmd_dickt = {
    "naiv": NaiveDijkstraAlgorithmStrategy,
    # "set": SetDijkstraAlgorithmStrategy
}


@click.group()
def main():
    pass


@main.command()
@click.option("--realiz", default="naiv")
@click.option("--vertex", default=0, type=int)
@click.option("--matrix", default=["0"], type=str, nargs=-1)
def dijkstra_algorithm(realiz: str, matrix: str, vertex: int) -> List[int]:
    matrix = make_matrix(matrix, vertex)

    answer = UseDijkstraAlgorithm(
        cmd_dickt[realiz]()
    ).search_shortest_path(matrix, vertex)

    return answer


@main.command()
@click.option("--start", default=1, type=int)
@click.option("--end", default=2, type=int)
@click.option("--step", default=1, type=int)
@click.option("--count", default=10, type=int)
def generate_data(start: int, end: int, step: int, count: int):
    generate_data_func(start, end, step, count)


@main.command()
@click.option("--realiz", default="naiv")
def measure_algo(realiz: str):
    func = UseDijkstraAlgorithm(
        cmd_dickt[realiz]()
    )

    measute_time_func(func)


@main.command()
@click.option("--file", type=click.Path())
def creat_chart(file: click.Path()):
    create_chart_func(file)
