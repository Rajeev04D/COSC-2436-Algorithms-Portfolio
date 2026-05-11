"""
Lab 2: Sorting Algorithms
Implements selection sort with performance tracking.
"""
from typing import List, Dict, Callable


def find_smallest_index(arr: List[Dict], key: Callable, start: int) -> int:
    smallest_idx = start
    smallest_val = key(arr[start])
    
    for i in range(start + 1, len(arr)):
        if key(arr[i]) < smallest_val:
            smallest_val = key(arr[i])
            smallest_idx = i
            
    return smallest_idx

def selection_sort(arr: List[Dict], key: Callable = lambda x: x, reverse: bool = False) -> List[Dict]:
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    result = arr.copy()
    
    for i in range(n - 1):
        extreme_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if (reverse and key(result[j]) > key(result[extreme_idx])) or (not reverse and key(result[j]) < key(result[extreme_idx])):
                extreme_idx = j
        
        if extreme_idx != i:
            result[i], result[extreme_idx] = result[extreme_idx], result[i]
            swaps += 1
    
    print(f"Selection Sort: {comparisons} comparisons, {swaps} swaps")
    return result


def python_builtin_sort(arr: List[Dict], key: Callable, reverse: bool = False) -> List[Dict]:
    """
    Python's built-in sort for comparison.
    Time Complexity: O(n log n) - Timsort algorithm
    """
    result = arr.copy()
    result.sort(key=key, reverse=reverse)
    print("Python Built-in Sort: O(n log n) - Timsort")
    return result
