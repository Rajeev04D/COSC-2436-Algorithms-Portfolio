# Lab 3: Recursion

## Student Information
- **Name:** [Rajeev Oad]
- **Date:** [2/14/2026]

## Recursion Concepts

### Two Parts of Every Recursive Function

1. **Base Case:**

 [Base case is something in a recursive function that does not allow recursive call. It is the least-common denominator of the problem since it can be solved immmediately without any more method calls. By making this function pay attention to the situation and handle it gracefully, we eliminate endless recursion and the resultant inevitable stack overflow.]

2. **Recursive Case:** 

[The base case is where the function doesn't call itself to solve a simpler form of the problem. This consists of solving a part of the problem and then calling the function for remaining. By reducing each call closer to the base case, the recursion guarantees movement towards a solution.]

### The Call Stack

[The call stack is a data structure which records the information of multiple function calls. A new “frame” is created in the stack every time that a function is called. This frame includes things such as the function arguments, and where to return to. After this function is done its frame comes off the stack. In recursion, you build additional frames every recursive call until you reach the terminating condition, after which the stack collapses on itself when going back.
Example: 

In fact(3), the stack grows as follows:

fact(3) calls fact(2)

fact(2) calls fact(1)

fact(1) returns 1, allowing fact(2) to return 2 * 1 = 2
Finally, fact(3) returns 3 * 2 = 6 as the stack unwinds.]

## Function Analysis

| Function | Base Case | Recursive Case | Time Complexity |
|----------|-----------|----------------|-----------------|
| countdown | i <= 0 | countdown(i-1) | O(n) |
| fact | x <= 1 | x * fact(x-1) | O(n) |
| recursive_sum | empty list | first + sum(rest) | O(n) |
| recursive_count | empty list | 1 + count(rest) | O(n) |
| recursive_max | single item | max(first, max(rest)) | O(n) |

## Reflection Questions

1. What happens if you forget the base case?
If you forget the base case, the recursion will continue indefinitely, leading to a stack overflow error because there is no condition to stop the recursive calls.

2. Why is the naive Fibonacci implementation inefficient?
The naive Fibonacci implementation is inefficient because it recalculates the same subproblems multiple times. This leads to an exponential time complexity of (O(2^n)), which is inefficient for large inputs.

3. Draw the call stack for fact(4).

fact(4)

fact(3)

fact(2)

fact(1)

Returns 1 (Base case)

Returns 2 * 1 = 2

Returns 3 * 2 = 6

Returns 4 * 6 = 24

This demonstrates how the call stack builds up with recursive calls and then unwinds as each function returns its result.