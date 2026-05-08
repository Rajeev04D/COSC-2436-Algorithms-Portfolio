# Knapsack Problem - Lab Report 11

## Name : Rajeev Oad

## Date : 4/23/2026

## Introduction
The knapsack problem is a classic optimization problem where you must select a combination of items with given weights and values to maximize the total value without exceeding a weight capacity. This problem is a perfect example of dynamic programming, breaking down a large problem into manageable subproblems.

## Objective
The goal of this lab is to implement the knapsack problem using dynamic programming to efficiently find the optimal combination of items that maximize the value within a specified weight limit.

## Implementation Details

### `calculate_total_value` Function
This function calculates the total value of a selected list of item names. It loops through the solution list, summing the values of the items.

### `knapsack` Function
- Builds a 2D grid where `grid[i][w]` represents the best list of items using the first `i` items with a weight capacity of `w`.
- Fills the grid dynamically by deciding whether to include or exclude each item based on weight constraints and maximizing value.

### `display_grid` Function
Formats and prints the grid with item names and values, showing how choices evolve as the capacity increases.

## Testing and Results

The program outputs the optimal item combinations for each weight capacity. Here is the expected output:
```text
                       1           2           3           4           5           6
GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)
LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)
iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
GOLD BAR       $30000(G)  $32000(iG) $33500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)
```
## Conclusion
This lab provided insight into dynamic programming through the knapsack problem. Implementing this approach efficiently finds the optimal solution without redundancy. Challenges included managing weight constraints and ensuring all possible combinations were considered.

## Code

```python
# ---------------------------------------------------------------------------
# PART 1 — helper function
# ---------------------------------------------------------------------------
def calculate_total_value(solution, items):
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total


# ---------------------------------------------------------------------------
# PART 2 — fill the DP grid
# ---------------------------------------------------------------------------
def knapsack(items, capacity):
    """
    Build a 2D grid where grid[i][w] is the best list of item names
    using only the first i items and a weight budget of w.
    """
    n = len(items)
    # grid[i][w] starts empty; we'll fill it row by row.
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                grid[i][w] = grid[i - 1][w][:]
            else:
                include_solution = grid[i - 1][w - weight][:] + [item_name]
                exclude_solution = grid[i - 1][w][:]
                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)
                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid


# ---------------------------------------------------------------------------
# PART 3 — pretty-print the grid
# ---------------------------------------------------------------------------
def display_grid(grid, items):
    n = len(items)
    cell_width = 12

    # Build the header row of capacity numbers (1..capacity)
    header = ""
    for w in range(1, len(grid[0])):
        header += "{:>{width}}".format(str(w), width=cell_width)

    print(" " * cell_width + header)

    for i in range(1, n + 1):
        # Start each data row with the item name, LEFT-aligned in cell_width.
        row = "{:<{width}}".format(items[i - 1][0], width=cell_width)

        for cell in grid[i][1:]:
            if cell:
                letters = "".join(name[0] for name in cell)
                value = calculate_total_value(cell, items)
                row += "{:>{width}}".format(f"${value}({letters})", width=cell_width)
            else:
                row += " " * cell_width

        print(row)


# ---------------------------------------------------------------------------
# PART 4 — run it
# ---------------------------------------------------------------------------
# Test data — do NOT modify these values.
items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6

# Call knapsack(items, capacity) and store the result in `grid`.
grid = knapsack(items, capacity)

# Display the finished grid.
display_grid(grid, items)
```
## Reflection Questions
1. What did this lab teach you about dynamic programming?

This lab helped me understand that dynamic programming is useful when a problem can be broken into smaller decisions. Instead of checking every possible combination from the beginning each time, the program stores previous results in a grid and builds on them. That made the knapsack problem easier to understand because I could see how each item and each capacity affected the final answer.
2. Why is the knapsack problem a good example of optimization?

The knapsack problem is a good example of optimization because the goal is not just to find any solution, but to find the best solution. The program has to choose items with the highest possible value without going over the weight limit. This showed me how algorithms can be used to make smart decisions when there are limits or constraints.
3. What was the most difficult part of this lab?

The most difficult part was understanding how the grid updates for each item and capacity. At first, it was confusing to see why the program compares including an item versus excluding it. After working through the table, it made more sense because each cell represents the best choice available at that point.
4. How did the grid help you understand the solution?

The grid made the process more visual because I could see the best item combinations changing as the weight capacity increased. Instead of only seeing the final answer, the table showed how the algorithm reached that answer step by step. This helped me understand that dynamic programming is based on building the final solution from smaller results.
5. Where could this type of algorithm be used in real life?

This type of algorithm could be used in situations where someone needs to choose the best combination of items under a limit. For example, it could help with packing a truck, choosing products within a budget, or selecting tasks when there is limited time. It is useful whenever there are multiple choices and a maximum capacity or restriction.
