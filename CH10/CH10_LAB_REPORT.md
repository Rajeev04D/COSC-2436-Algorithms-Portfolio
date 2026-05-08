# Lab Report#10

**Student Information**

**Name:** [Rajeev Oad]

**Date:** [4/16/2026]

**Algorithm Analysis:** Greedy Truck Packing Algorithm

**Algorithm Understanding**

**What type of problem is this algorithm solving?**

This algorithm addresses an optimization and packing problem.

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**

No, greedy algorithms do not always guarantee an optimal solution because they make local best choices that may not lead to the global best outcome.

**What is the greedy choice made in this algorithm?**

The algorithm chooses to pack the largest boxes by volume first.

# Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
Sorting in descending order ensures that larger boxes are prioritized to maximize space utilization.

**What would happen if we sorted the boxes in ascending order instead?**  
This could lead to inefficient packing, as smaller boxes might occupy space that larger boxes could fill more efficiently.

**Why do we keep track of `used_volume`?**  
Tracking `used_volume` ensures that we do not exceed the truck's volume capacity when packing boxes.

---

# Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
Boxes must fit physically within the truck's specific dimensions, not just by volume.

**Give an example where a box fits by volume but not by dimensions.**  
A long, flat box may fit by volume but be too lengthy for the truck's dimensions.

**How would you modify the algorithm to check dimension constraints before packing a box?**  
Before adding a box, compare its dimensions with the truck's dimensions to ensure it fits.

---

# Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
The greedy approach might leave unused space that smaller boxes could have utilized more efficiently.

**How is this problem related to the Knapsack Problem?**  
It's similar as both involve choosing items to maximize usage under constraints.

**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
Dynamic programming could provide an optimal solution but with higher time complexity.

**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
The algorithm must consider both weight and volume constraints before adding a box.

**Why are greedy algorithms often preferred despite not always being optimal?**  
They are straightforward and fast, providing good enough solutions quickly.