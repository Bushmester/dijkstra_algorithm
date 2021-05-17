from numpy import median
import pandas as pd
import matplotlib.pyplot as plt


def create_chart(csv_file_path: str):
    data = pd.read_csv(csv_file_path)
    data.set_index("size", inplace=True) 
    data = data.sort_values("size")

    plt.plot(data["min"], color="#008000", label="min")
    plt.plot(data["max"], color="#ff0000", label="max")
    plt.plot(data["avg"], color="#ffa500", label="avg")
    plt.plot(data["median"], color="#8b00ff", label="median")

    plt.legend()
    plt.savefig("mygraph.png")

PATH = "/home/bushmester/study/study_programming/cpp/dijkstra-algorithm/work_with_data/load_testing_mesurenets/1621278390.2586138.csv"
create_chart(PATH)