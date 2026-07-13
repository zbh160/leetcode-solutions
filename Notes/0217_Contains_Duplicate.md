# References

- LeetCode: https://leetcode.com/problems/contains-duplicate/
- GitHub: TODO
- YouTube: TODO

---

# Problem Breakdown

## Goal

Given an integer array `nums`, determine whether any value appears at least twice.

## Constraints

- Return `True` if a duplicate exists; otherwise `False`.
- Target complexity: `O(n)`.

---

# Core Idea

## Pattern

Hash Set

## Key Insight

Store previously seen numbers in a hash set. If the current number already exists in the set, return `True`; otherwise, add it and continue.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

---

# Core Code

```python
num_show = set()

for num in nums:
    if num in num_show:
        return True
    num_show.add(num)

return False
```

## Why this code matters

- Hash set lookup is **O(1)** on average.
- Each element is processed once.
- Early exit when a duplicate is found.

---

# Takeaways

## Interview Tips

- Explain the brute-force approach before optimizing.
- A set is sufficient because only existence checking is required.

## Common Pitfalls

- Using a list for lookups.
- Sorting first.
- Forgetting to add the current number after checking.

## Personal Notes

- Use a **set** when you only need to check whether a value has been seen before.
- A **set** provides **O(1)** average lookup time, while searching an array requires **O(n)** time.
- Choose a **dictionary** when you need to map keys to values; choose a **set** when you only need existence checking.

## Related Problems

- Two Sum
- Contains Duplicate II
- Contains Duplicate III
- Happy Number
- Longest Consecutive Sequence
