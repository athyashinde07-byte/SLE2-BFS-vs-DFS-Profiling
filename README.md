# SLE-2: BFS vs DFS Profiling

Student: Atharv Deepak Shinde
PRN: 25UAM061
Course: 02AML204 – Introduction to Artificial Intelligence

## Objective
Compare Breadth-First Search (BFS) and Depth-First Search (DFS) on the same grid-maze problem using empirical profiling.

## Profiling
The project uses Python timeit for runtime measurement and a manual counter for expanded nodes. Both algorithms use the same graph, start node and goal node.

Problem: 40 x 40 open grid
Start: node 0
Goal: node 1599
Timing: 5 batches x 100 repetitions

## Files
- bfs_dfs_profiling.py: BFS, DFS and profiling code
- profiling_results.txt: measured benchmark output
- SLE2_Report.md: completed SLE-2 report
- AI_Contribution_Log.md: AI contribution record
- requirements.txt: dependency note

## Run
python3 bfs_dfs_profiling.py

No external packages are required.

Note: Runtime depends on the computer, Python version and system load. The included values are from one reproducible benchmark run and should be rerun on the student's computer if the instructor requires machine-specific measurements.
