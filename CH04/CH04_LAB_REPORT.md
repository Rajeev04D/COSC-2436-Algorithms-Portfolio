# Lab 04: Quicksort

## Student Information
- **Name:** Rajeev Oad
- **Date:** 2/20/2026

## Quicksort Concepts

### Divide and Conquer
Quicksort uses divide-and-conquer by breaking a big sorting problem into smaller ones. It picks one element as a pivot, splits the list into two parts (values smaller than the pivot and values bigger than the pivot), then sorts those parts the same way. When the small parts are sorted, putting them together with the pivot in the middle gives a sorted list.

### The Three Steps
1. **Choose pivot:** Pick one element (often first, last, or random). The pivot is the “reference point” we compare everything to.
2. **Partition:** Go through the remaining elements and separate them into:

less: values < pivot

greater: values > pivot (sometimes >= pivot depending on the version)

3. **Recurse and combine:** Run quicksort on less and greater, then combine like:
sorted = quicksort(less) + [pivot] + quicksort(greater)

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
Trace: quicksort([3, 5, 2, 1, 4])

Call 1: quicksort([3, 5, 2, 1, 4])

pivot = 3

less = [2, 1]

greater = [5, 4]
→ result = quicksort([2, 1]) + [3] + quicksort([5, 4])

Call 2 (left side): quicksort([2, 1])

pivot = 2

less = [1]

greater = []
→ result = quicksort([1]) + [2] + quicksort([])

Call 3: quicksort([1])

base case (already sorted) → [1]

Call 4: quicksort([])

base case → []

So left side becomes: [1] + [2] + [] = [1, 2]

Call 5 (right side): quicksort([5, 4])

pivot = 5

less = [4]

greater = []
→ result = quicksort([4]) + [5] + quicksort([])

Call 6: quicksort([4])

base case → [4]

Call 7: quicksort([])

base case → []

So right side becomes: [4] + [5] + [] = [4, 5]

Final combine:
left + pivot + right
[1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | Pivot splits the array into two equal halves each time, so recursion depth is log n and each level does about n work. |
| Average | O(n log n) | On average, pivots split the list “pretty evenly,” so it behaves close to the best case most of the time. |
| Worst | O(n²) | Pivot keeps giving very uneven splits (like 0 and n−1), causing deep recursion and repeated comparisons. |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?

You get the worst case: one side becomes empty and the other side has almost everything, so it takes O(n²) time.

2. How could you improve pivot selection to avoid worst-case performance?

Use a random pivot, middle element, or median-of-three (first, middle, last) to reduce the chance of bad splits.

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?

Quicksort is usually much faster than bubble sort (which is often O(n²)).

Compared to merge sort, quicksort is often faster in practice and uses less extra memory, but merge sort guarantees O(n log n) worst-case.

4. Why do we use `array[1:]` instead of `array` when building the less and greater lists?

Because array[0] is the pivot. If we loop over the full array, we might compare the pivot with itself and accidentally place it into less or greater, which can mess up the recursion or cause duplicates.