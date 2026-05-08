## Lab Report 08

### Student Information
- **Name:** [Rajeev Oad]
- **Date:** [4/2/2026]

### Algorithm Analysis

#### AVL Trees
- **Balance Factor Range:** [ The balance factor in an AVL tree can be -1, 0, or 1. This means a node is balanced if the height difference between its left and right subtrees is within this range.]
- **Why rebalance?** [Rebalancing ensures that the AVL tree maintains a height of (O(\log n)). This keeps operations like search, insertion, and deletion efficient, avoiding the (O(n)) time complexity that can occur in an unbalanced tree.]
- **Time Complexity (all operations):** [(O(\log n)). This includes insertion, deletion, and lookup operations, due to the tree being balanced]

#### Rotation Cases
| Case | Imbalance | Fix |
|------|-----------|-----|
| LL   |Left-Left  |Right rotate the unbalanced node|
| RR   |Right-Right|Left rotate the unbalanced node|
| LR   |Left-Right |Left rotate the left child, then right rotate the unbalanced node|
| RL   |Right-Left |Right rotate the right child, then left rotate the unbalanced node|

### Reflection Questions

1. Why is an unbalanced BST bad?
[An unbalanced BST can degrade into a linked list in the worst case, making search operations (O(n)) instead of (O(\log n)).]
2. How do rotations maintain the BST property?
[Rotations adjust the subtree structure while preserving the in-order sequence of nodes, ensuring that left descendants remain less than the parent and right descendants remain greater.]
3. What other self-balancing trees exist?
[Other self-balancing trees include Red-Black Trees, Splay Trees, and B-Trees, each with their own balancing strategies and use cases.
]