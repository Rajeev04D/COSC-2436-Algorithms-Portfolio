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