import heapq
from math import inf


def set_dijkstra(matrix, vertex):
    ver_count = len(matrix)
    dist = [inf] * ver_count
    dist[vertex] = 0
    visited = set()
    pq = [(0, vertex)]

    while len(pq) != 0:
        current_len, ver = heapq.heappop(pq)

        if current_len > dist[ver] or ver in visited:
            continue

        for i in range(ver_count):
            to_ver = i
            current_len = matrix[ver][to_ver]

            if dist[to_ver] > current_len + dist[ver] and current_len > 0:
                dist[to_ver] = current_len + dist[ver]
                heapq.heappush(pq, (dist[to_ver], to_ver))

        visited.add(ver)

    return dist
