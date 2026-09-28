from collections import deque
import statistics
import timeit

GRID_SIZE = 40
START = 0
GOAL = GRID_SIZE * GRID_SIZE - 1

def build_grid_graph(size):
    graph = {node: [] for node in range(size * size)}
    for row in range(size):
        for col in range(size):
            node = row * size + col
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < size and 0 <= nc < size:
                    graph[node].append(nr * size + nc)
    return graph

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    expanded = 0
    while queue:
        node = queue.popleft()
        expanded += 1
        if node == goal:
            return expanded
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return expanded

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    expanded = 0
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        expanded += 1
        if node == goal:
            return expanded
        for neighbour in reversed(graph[node]):
            stack.append(neighbour)
    return expanded

def profile_algorithm(function, graph, start, goal, repetitions=100):
    timings = timeit.repeat(lambda: function(graph, start, goal), repeat=5, number=repetitions)
    average_ms = statistics.mean(timings) / repetitions * 1000
    std_dev_ms = statistics.stdev(timings) / repetitions * 1000
    expanded_nodes = function(graph, start, goal)
    return average_ms, std_dev_ms, expanded_nodes

def main():
    graph = build_grid_graph(GRID_SIZE)
    bfs_time, bfs_std, bfs_nodes = profile_algorithm(bfs, graph, START, GOAL)
    dfs_time, dfs_std, dfs_nodes = profile_algorithm(dfs, graph, START, GOAL)
    print('SLE-2: BFS vs DFS Profiling')
    print('=' * 35)
    print(f'Grid size: {GRID_SIZE} x {GRID_SIZE}')
    print(f'Start node: {START}')
    print(f'Goal node: {GOAL}')
    print('Timing: 5 batches x 100 repetitions\n')
    print('BFS')
    print(f'Average time: {bfs_time:.6f} ms/run')
    print(f'Standard deviation: {bfs_std:.6f} ms/run')
    print(f'Nodes expanded: {bfs_nodes}\n')
    print('DFS')
    print(f'Average time: {dfs_time:.6f} ms/run')
    print(f'Standard deviation: {dfs_std:.6f} ms/run')
    print(f'Nodes expanded: {dfs_nodes}')

if __name__ == '__main__':
    main()
