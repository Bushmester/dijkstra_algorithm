# Fucking Dijkstra's algorithm

This algorithm searches for the shortest path from the start node to all vertices.
He will help if you need to determine the shortest road, the price of a trip with transfers 

### Examples of using the algorithm in everyday life 
There are a number of flights between cities in the world, for each the cost is known. The cost of a flight from A to B may not be equal to the cost of a flight from B to A. Find the minimum cost route (possibly with transfers) from Almetyevsk to Sim? 

### Naive implementation 
##### How the algorithm works
The source code is located  ```dijkstra-algorithm/dijkstra_algorithm/dijkstra_strategy.py``` in class ```NaiveDijkstraAlgorithmStrategy```

To begin with, we will pass our function an adjacency matrix and a vertex from which we will look for the shortest paths to other vertices. 

Let's get a list of shortest paths and checked vertices. Let's fill the shortest paths with infinitely large numbers, not forgetting to assign the vertex from which we are looking for paths - zero, and drop this vertex into the list of checked ones.

Further, while we have unchecked vertices, we rotate in a cycle. In it, we make a passage from our top to others that have a connection with our node. If the vertex is not checked and its path is less than in our shortest paths, then we reassign to it the sum of the weight of the original vertex and its path.

The next step is to find the vertex with the minimum weight and reassign the vertex.

Thus, we check all the vertices and return the list of shortest paths. PROFIT! 

##### Pros:
- simple implementation

##### Minuses:
- does not work with negative values
- asymptotic complexity O (n ^ 2) 

### Implementation through sets
The source code is located  ```dijkstra-algorithm/dijkstra_algorithm/dijkstra_strategy.py``` in class ```SetDijkstraAlgorithmStrategy```

It should be noted right away that the Python implementation uses ```heapq``` - a priority queue. This is done so that you can sort pairs (in the case of Python - tuples) by the first element, which allows sets, for example, in C ++. 

To begin with, we will pass our function an adjacency matrix and a vertex from which we will look for the shortest paths to other vertices. 

Let's get a list of shortest paths and checked vertices. Let's fill the shortest paths with infinitely large numbers, not forgetting to assign the vertex from which we are looking for 0 paths. We also create a priority queue with paths, in which we put the path to the current vertex so that the loop can start working. 

In the cycle, we pull out the shortest path and the vertex to which it leads, and check if this vertex has not been visited. If visited, then skip the current iteration. 

If not, then we take the vertex we just arrived at, and in the loop add to the queue those paths that are shorter than the ones already written, and update the dist list with the path lengths. 

At the end of the while loop, add the vertex to the set of visited ones.

At the end of the while loop, we return a list with the lengths of paths to all vertices. 

##### Pros:
- automatically follows the shortest path of all possible
- uses only potentially useful paths
- no need to redefine ```vertex``` 
- asymptotic complexity O (n * log(n))


### Installation
You need at least `Python 3.8` and `pip` installed to run this CLI tool.
1. Install it using `pip`
    ```shell
    pip install dijkstra-algorithm 
    ```
2. Call `--help` to ensure that it is successfully installed
    ```shell
    fucking-dijkstra  --help
    ```
3. In the .env files, create the constants `TESTING_DATA` (the directory for the generated test data) and `MEASUREMENTS` (the directory for the measured data). 

### Available commands

1. `dijkstra-algorithm`
finding the shortest path with Dijkstra's algorithm.
Takes the number of vertices, the start node and the matrix.
2. `generate-data`
generates an input matrix and a random start node. Accepts optionally `--start`, `--end`, `--step`, and `--count` of files to create.
3. `measure-algo`
measures the execution time of an algorithm and outputs them to a csv file.
4. `creat-chart` 
renders data from csv file. Take path to csv file

### Optional parameters
`--realiz` for `dijkstra-algorithm` and `measure-algo`. Has implementations: naive (by default) and through sets.

### For more precise information enter 

```
fucking-dijkstra command-name --help
```

## Asymptotic computational complexity

Looking at the resulting graphs, we note that they coincide with the assumed asymptotic complexity in time, from which we can conclude that our utility is working successfully. 

### Naive implementation O(n ^ 2)
![naiv](dijkstra_algorithm/work_with_data/load_testing_mesurenets/load_testing_naiv_measurements/naiv_graph.png)

### Set implementation O(n * log(n))
![set](dijkstra_algorithm/work_with_data/load_testing_mesurenets/load_testing_set_measurements/set_graph.png)


[Video tutorial in Russian](https://www.youtube.com/watch?v=IhhajO5wVOA)