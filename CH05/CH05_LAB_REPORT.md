# Lab 05: 2436 Hash Table Lab 

## Student Information
- **Name:** Rajeev Oad
- **Date:** 2/26/2026

## Key Concepts
Hash Table Concepts:
Structure: Stores key-value pairs, using a hash function to determine the index.
Hash Function: Converts keys into an index for storage.
Collision Handling: Uses linear probing, checking the next available slot if a collision occurs.
Efficiency: Average insert/search operations are O(1), meaning fast access.

## What I Learned
In this lab, I learned how hash tables efficiently store and retrieve key-value pairs using hash functions to compute indices. The implementation involved handling collisions through linear probing, which taught me how to manage potential conflicts when different keys map to the same index. This experience improved my understanding of Python, particularly in using classes and functions to create data structures. Additionally, I appreciated the balance between the average O(1) time complexity and the challenges posed by collisions, enhancing my grasp of algorithm efficiency.

## Challenges
In this lab, the most difficult part was likely handling collisions effectively within the hash table. Managing cases where multiple keys hash to the same index required understanding and implementing linear probing. I overcame this challenge by thoroughly understanding how linear probing works and ensuring my insert and search methods correctly handle such situations. Testing with various scenarios helped me confirm that the implementation worked as expected.

## Reflection Questions
## 1. What are the advantages of using a hash table?
Fast Access: Offers average-case constant-time complexity, O(1), for insert and search operations.
Efficiency: Ideal for quick lookups and retrievals in large datasets.
## 2. How does the hash function affect the performance of a hash table?
Distribution: A good hash function distributes keys uniformly across the table, minimizing collisions.
Efficiency: Poor hash functions can lead to more collisions, increasing lookup time to O(n) in the worst case.
## 3. What are other collision resolution techniques besides linear probing?
Chaining: Stores collided elements in a linked list at each index.
Double Hashing: Uses a second hash function to determine step size for probing.
Quadratic Probing: Uses quadratic functions to calculate the next slot in case of collisions.