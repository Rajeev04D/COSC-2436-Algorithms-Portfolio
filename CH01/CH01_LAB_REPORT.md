# Chapter 1 Lab Report: Binary Search

## Student Information
- **Name:** [Rajeev Oad]
- **Date:** [5/8/2026]
- **Course:** COSC 2436

## Algorithm Summary

### Linear Search
[Linear search iterates through each element in an array until it finds the target or reaches the end. It has a time complexity of \(O(n)\). Use it for unsorted or small datasets where ease of implementation is a priority.]
### Binary Search
[Binary search requires a sorted array and works by repeatedly dividing the search interval in half, quickly narrowing down the position of the target. It has a time complexity of \(O(\log n)\) and is ideal for large sorted datasets.]

## Test Results
```
Here is the output from the program, showing timing comparisons between linear and binary search:

Binary Search vs Linear Search Time Comparison
================================================
Searching in a sorted list of 128 numbers

Searching for: 1
Linear search time: 0.00000882 seconds
Binary search time: 0.00000548 seconds
Linear search result: 0
Binary search result: 0
Binary search is 1.61x faster

Searching for: 64
Linear search time: 0.00000405 seconds
Binary search time: 0.00000119 seconds
Linear search result: 63
Binary search result: 63
Binary search is 3.40x faster

Searching for: 128
Linear search time: 0.00000358 seconds
Binary search time: 0.00000215 seconds
Linear search result: 127
Binary search result: 127
Binary search is 1.67x faster

Searching for: 50
Linear search time: 0.00000215 seconds
Binary search time: 0.00000167 seconds
Linear search result: 49
Binary search result: 49
Binary search is 1.29x faster

Searching for: 100
Linear search time: 0.00000238 seconds
Binary search time: 0.00000095 seconds
Linear search result: 99
Binary search result: 99
Binary search is 2.50x faster

Searching for: 25
Linear search time: 0.00000262 seconds
Binary search time: 0.00000191 seconds
Linear search result: 24
Binary search result: 24
Binary search is 1.38x faster

Searching for: 75
Linear search time: 0.00000191 seconds
Binary search time: 0.00000167 seconds
Linear search result: 74
Binary search result: 74
Binary search is 1.14x faster

Searching for: 10
Linear search time: 0.00000143 seconds
Binary search time: 0.00000167 seconds
Linear search result: 9
Binary search result: 9
Binary search is 0.86x faster

Searching for: 90
Linear search time: 0.00000238 seconds
Binary search time: 0.00000095 seconds
Linear search result: 89
Binary search result: 89
Binary search is 2.50x faster

Searching for: 200
Linear search time: 0.00000286 seconds
Binary search time: 0.00000119 seconds
Linear search result: None
Binary search result: None
Binary search is 2.40x faster

Lab Challenge Answer:
Maximum steps for binary search in 128 items:
log2(128) = 7 steps maximum