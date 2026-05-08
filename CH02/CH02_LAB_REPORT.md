## Lab Report 02

### Student Information
- **Name:** Rajeev
- **Date:** 2/8/2026

### Algorithm Analysis

#### Selection Sort
- **Time Complexity:** O(n²)
- **How it works:** Selection sort goes through the list, finds the smallest value, and swaps it into the correct spot. Then it repeats for the next position until everything is sorted.

#### Arrays vs Linked Lists

| Operation | Array  |  Linked List  |   Why? |
|-----------|------- |------------- |------|
| Read      |   Fast(O(1))     |          Fast (O(1))       |   Arrays can jump to an index, but linked lists have to move through nodes.   |
| Insert    |  Slower (O(n))     |   Faster (O(1) if positioned)          | Arrays usually shift elements, linked lists just change pointers.     |
| Delete    |   Slower (O(n))    |       Faster (O(1) if positioned)      |  Arrays shift elements after deleting, linked lists reconnect pointers.   |

### Reflection Questions

1. Why is selection sort O(n²)?
Selection sort is O(n²) because for every element, it still has to scan the rest of the list to find the smallest one, so the comparisons add up a lot.
2. When would you choose a linked list over an array?
I’d pick a linked list when I need a lot of inserting/deleting and the size changes often, and I don’t really need quick index access.