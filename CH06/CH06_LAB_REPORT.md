# Lab 06: 2436 Ch06

## Student Information
- **Name:** [Rajeev Oad]
- **Date:** [3/5/2026]

## Key Concepts
[In this lab, I explored the application of the Breadth-First Search (BFS) algorithm on a graph representing Texas road networks. BFS is effective for finding the shortest path by the number of edges due to its level-order traversal using a queue. This lab reinforced my understanding of graph data structures, specifically how adjacency lists are utilized for efficient storage. Implementing BFS helped me grasp its time complexity (O(V + E)) and practical applications. A key challenge was ensuring correct graph traversal and pathfinding, which I overcame with careful attention to queue manipulation and edge relationships. Overall, the lab enhanced my comprehension of BFS and its ability to efficiently explore unweighted graphs.]

## What I Learned
[uring this lab, I deepened my understanding of graph data structures, particularly the efficiency of adjacency lists in representing networks. Implementing the Breadth-First Search (BFS) algorithm helped me grasp how to explore nodes level by level using a queue, ensuring the shortest path by the number of edges is found. I also learned about BFS's time complexity of (O(V + E)), reinforcing its utility in unweighted graphs. This exercise improved my skills in both graph traversal and pathfinding, preparing me for more complex algorithms.

## Challenges
One of the most difficult parts of this lab was ensuring correct graph traversal and pathfinding using the BFS algorithm. Implementing the queue for BFS required careful attention to ensure nodes were processed in the correct order, reflecting BFS's level-order traversal. Debugging was also challenging, particularly when paths did not generate as expected. I tackled these issues by reviewing the algorithm's logic, checking edge cases, and using print statements to trace the program's execution. This methodical approach helped me identify mistakes in queue manipulation and verify that all nodes were being correctly visited. Overcoming these obstacles reinforced my understanding of BFS and its applications in graph traversal.]

## Reflection Questions
## 1. Why does BFS use a queue instead of a stack?

BFS uses a queue to ensure that nodes are processed in the order they are discovered, exploring each level of a graph fully before moving to the next. This level-order traversal is key for BFS to find the shortest path by number of edges in an unweighted graph.

## 2. Whats the difference between BFS shortest path and actual shortest distance?

The shortest path in BFS refers to the path with the fewest edges between two nodes. Actual shortest distance involves the shortest path calculated with edge weights considered, which requires algorithms like Dijkstra's that accommodate weighted graphs.

## 3. When would you use BFS vs DFS?

## BFS: 
Use BFS when you need the shortest path in terms of edges, or when exploring nodes level by level is important, like in unweighted graphs or finding connected components.
## DFS: 
Use DFS when you're searching paths in a more exploratory depth-first manner, such as finding connected components in graphs, performing topological sorts, or solving puzzles like mazes.