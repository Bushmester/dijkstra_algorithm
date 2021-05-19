import click

from typing import List, Tuple

from dijkstra_algorithm.dijkstra_strategy import UseDijkstraAlgorithm, NaiveDijkstraAlgorithmStrategy, SetDijkstraAlgorithmStrategy
from dijkstra_algorithm.functions.make_matrix import make_matrix
from dijkstra_algorithm.work_with_data.generate_data import generate_data_func
from dijkstra_algorithm.work_with_data.measure_time import measute_time_func
from dijkstra_algorithm.work_with_data.create_chart import create_chart_func


cmd_dickt = {
    "naiv": NaiveDijkstraAlgorithmStrategy,
    "set": SetDijkstraAlgorithmStrategy
}


@click.group()
def main():
    pass


@main.command()
@click.option("--realiz", default="naiv")
@click.argument("vertex", type=int)
@click.argument("start_node", type=int)
@click.argument("matrix_el", type=int, nargs=-1)
def dijkstra_algorithm(realiz: str, matrix_el: Tuple[int], vertex: int, start_node: int) -> List[int]:

    matrix = make_matrix(matrix_el, vertex)

    answer = UseDijkstraAlgorithm(
        cmd_dickt[realiz]()
    ).search_shortest_path(matrix, start_node)

    print(answer)


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
@click.argument("file", type=click.Path())
def creat_chart(file: click.Path()):
    create_chart_func(file)
