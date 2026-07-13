# References

- LeetCode: https://leetcode.com/problems/product-of-array-except-self/
- GitHub: TODO
- YouTube: TODO

---

# Problem Breakdown

## Goal

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of all elements in `nums` except `nums[i]`.

## Constraints

- Do not use division.
- Solve the problem in `O(n)` time.
- Use `O(1)` extra space, excluding the output array.

---

# Core Idea

## Pattern

Prefix & Suffix

## Key Insight

For each index, the answer is the product of all elements before the current index and all elements after it. Use two passes: first store prefix products in `result`, then traverse backward and multiply suffix products into `result`.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(1)` excluding the output array

---

# Core Code

```python
result = [1] * len(nums)

prefix = 1
for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(len(nums) - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

return result
```

## Why this code matters

- The first loop stores the product of all values before each index.
- The second loop multiplies the product of all values after each index.
- Reusing `result` avoids separate prefix and suffix arrays.
- The current value is excluded because `prefix` and `suffix` are applied before being updated with `nums[i]`.

---

# Takeaways

## Interview Tips

- Mention the division-based idea first, then explain why it is not allowed.
- Explain the formula: `result[i] = prefix product × suffix product`.
- Point out that the output array does not count as extra space.

## Common Pitfalls

- Using division.
- Updating `prefix` before assigning it to `result[i]`.
- Updating `suffix` before multiplying it into `result[i]`.
- Traversing the suffix pass in the wrong direction.
- Creating separate prefix and suffix arrays when `O(1)` extra space is required.

## Personal Notes

### Step 1: Build Prefix Products

- Create a result array of `1 * len(nums)`.
- Traverse from left to right.
- Store the current prefix product in `result[i]`.
- Keep updating the running prefix with `prefix *= nums[i]`.

```python
result = [1] * len(nums)

prefix = 1
for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]
```

### Step 2: Multiply by Suffix Products

- Traverse from right to left.
- Multiply the current suffix into `result[i]`.
- Keep updating the running suffix with `suffix *= nums[i]`.

```python
suffix = 1
for i in range(len(nums) - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]
```

### Key Memory Rule

- Pass 1: Fill `result` with prefix products.
- Pass 2: Multiply suffix products into `result`.
- `prefix` contains everything before index `i`.
- `suffix` contains everything after index `i`.

## Related Problems

- Trapping Rain Water
- Maximum Product Subarray
- Range Sum Query
- Running Sum of 1D Array
- Maximum Difference Between Increasing Elements
