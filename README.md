# maze_navigator

## Problem

given a start coordinate, finish coordinate, and coordinates of many barriers, find a path from the start to the finish.

## Solution

- written in python
- implements a heuristic search algorithm using manhattan distance to the finish to select path
- implemented using a priority queue, visited, and node data structures
- after visited a node, the node because closed or visited
- nodes are only re-opened if a shoter path is found to that node / state
- if we find a node that is already open, update path if shorter, else do nothing
- prints visual output of the maze and path for ease of understanding
