"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.
"""
from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    if start not in graph.vertices or end not in graph.vertices:
        return None

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    if start not in graph.vertices:
        return {}

    distances = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    path = bfs_find_path(graph, v1, v2)
    return path is not None
