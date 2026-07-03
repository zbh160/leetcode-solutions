# References

- LeetCode: https://leetcode.com/problems/two-sum/description/
- GitHub: TODO
- YouTube: https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf

---

# Problem Breakdown

## Goal

Given an integer array `nums` and an integer `target`, find the indices of the two numbers whose sum equals `target`. Each input is guaranteed to have exactly one valid solution, and the same element cannot be used twice.

## Constraints

- Exactly one valid solution exists.
- Return the indices, not the values.
- The order of the returned indices does not matter.
- The optimal solution should run in `O(n)` time.

---

# Core Idea

## Pattern

Hash Map

## Key Insight

Traverse the array once while storing previously visited numbers and their indices in a hash map. For each number, calculate its complement (`target - num`) and check if it has already been seen.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

---

# Core Code

```python
hashmap = {}

for i, num in enumerate(nums):
    diff = target - num
    if diff in hashmap:
        return [hashmap[diff], i]
    hashmap[num] = i

return []
```

## Why this code matters

- Hash map provides O(1) average lookup.
- Check for the complement before inserting.
- Solve the problem in one pass.

---

# Takeaways

## Interview Tips

- Explain the brute-force solution before the optimized one.
- Mention the time-space tradeoff.
- Explain why one pass is sufficient.

## Common Pitfalls

- Inserting before checking.
- Returning values instead of indices.
- Reusing the same element.

## Personal Notes

-

## Related Problems

- Contains Duplicate
- Contains Duplicate II
- Two Sum II - Input Array Is Sorted
- 3Sum
- 4Sum
