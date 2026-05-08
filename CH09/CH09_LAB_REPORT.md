
**Lab Report 09 — Dijkstra's Shortest Path**

**Student Information**

Name: [Rajeev Oad]
Date: [4/9/2026]
**Algorithm Analysis: Dijkstra's Algorithm**

**What type of graph does this program build?** [Undirected, weighted]
**Why must all edge weights be non-negative for Dijkstra's to work?** [Dijkstra's algorithm assumes that once a node's shortest path is found, it will not change. Negative weights can create cycles that continuously reduce the path cost, invalidating this assumption.]
**Time Complexity (with simple array scan for min-node):** (O(V^2)), where (V) is the number of vertices.
**Time Complexity (with a min-heap/priority queue):** (O((V + E) \log V)), where (E) is the number of edges.
Core Data Structures
Core Data Structures

|**Structure**|	**Variable Name** |	                **What It Stores**               |
|--------------|------------------|--------------------------------------------------|
|Adjacency dict|	graph	      |  Connections and weights between nodes           |
|Cost table    |	costs	      | Cheapest known cost to reach each node from start|
|Parent table  |	parents	      |  Parent nodes to trace the shortest path         |
|Visited list  |   processed      | Nodes whose shortest path has been finalized     | 
Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

| **Iteration** | **Current Node **| **costs[A]** | **costs[B]** |** costs[C]** | **costs[D]** | **processed **  |
|---------------|------------------|--------------|--------------|--------------|--------------|-----------------|
| Init          | —                | 0            | ∞            | ∞            | ∞            | —               |
| 1             | A                | 0            | 1            | 4            | ∞            | A               |
| 2             | B                | 0            | 1            | 3            | 7            | A, B            |
| 3             | C                | 0            | 1            | 3            | 6            | A, B, C         |
| 4             | D                | 0            | 1            | 3            | 6            | A, B, C, D      |
Shortest path A to D: [A -> B -> C -> D]
Total cost: [6]

**Reflection Questions**

**Why does the algorithm initialize all node costs to infinity except the start node?**
To reflect initial uncertainty about the path lengths, except for the start node where the cost is known to be zero.

**Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?**
To enable easy traversal in undirected graphs. Not doing so would prevent bidirectional path findings.

**The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?**
It reduces time complexity for finding the minimum cost unprocessed node, which is crucial for large graphs.

**If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?**
They could cause incorrect shortest paths due to path cost reductions from negative cycles. The Bellman-Ford algorithm handles negative weights.

**How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?**
It tracks the previous node on the shortest path, allowing backward reconstruction. Reversing it provides the correct start-to-end order.


**What happens when the source and destination are in disconnected components of the graph? How does the code detect this?**
If nodes remain with infinite costs, it's detected as unreachable, and the code returns None, None for path and cost.