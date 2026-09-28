# SLE-2: Profiling Report

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM061  
**Name:** Atharv Deepak Shinde  
**Division:** A / B  
**Date:** 28/09/2026  
**GitHub Link:** https://github.com/athyashinde07-byte/SLE2-BFS-vs-DFS-Profiling

## 1. Algorithms / Versions Profiled

### Algorithm A – Breadth-First Search (BFS)
BFS explores the search space level by level using a queue.

### Algorithm B – Depth-First Search (DFS)
DFS explores one path deeply before backtracking using a stack.

Both algorithms were tested on the same 40 x 40 open grid, with start node 0 and goal node 1599.

## 2. Profiling Method

Python timeit was used for execution-time measurement. A manual counter was used to count expanded nodes.

Experiment settings:
- Grid: 40 x 40
- Start: 0
- Goal: 1599
- Timing: 5 batches x 100 repetitions
- Same graph and traversal order for both algorithms

## 3. Results

| Metric | BFS | DFS |
|---|---:|---:|
| Average runtime (ms/run) | 0.873661 | 0.047233 |
| Standard deviation (ms/run) | 0.210214 | 0.008218 |
| Nodes expanded | 1600 | 79 |

## 4. Justification & Analysis

BFS expanded 1600 nodes, while DFS expanded 79 nodes in this particular experiment. The measured average runtime was 0.873661 ms/run for BFS and 0.047233 ms/run for DFS.

The difference is related to the search order. BFS systematically explores nodes level by level, while DFS follows a path deeply before backtracking. With the fixed neighbour order used in this experiment, DFS reached the goal after fewer expansions.

This is a result for the selected test case, not a universal claim that DFS is always faster than BFS. A different graph, goal position, obstacle layout or traversal order can produce different measurements.

## 5. AI Contribution Note

AI assistance was used to understand the SLE-2 requirements, structure the BFS/DFS profiling program, explain the profiling method, and prepare the report format.

The student reviewed the material, selected the BFS-vs-DFS experiment, ran the program, checked the output, and used the measured results in the report.

## 6. Conclusion

BFS and DFS were profiled on the same 40 x 40 grid-search problem. In the measured run, DFS expanded fewer nodes and had a lower average execution time than BFS. The experiment demonstrates empirical comparison using runtime and state-expansion data.
