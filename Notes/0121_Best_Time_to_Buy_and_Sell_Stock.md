# References

- LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- GitHub: TODO
- YouTube: TODO

---

# Problem Breakdown

## Goal
Given an array `prices`, determine the maximum profit from one buy and one sell transaction.

## Constraints
- One transaction only.
- Buy before selling.
- Return `0` if no profit is possible.
- Target: `O(n)`.

---

# Core Idea

## Pattern
Greedy (Running Minimum)

## Key Insight
Track the minimum price seen so far. For each price, compute today's profit and update the best profit.

## Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`

---

# Core Code

```python
max_profit = 0
min_price = float('inf')

for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

return max_profit
```

## Why this code matters

- Keeps the lowest buying price.
- Computes the best selling profit in one pass.

---

# Takeaways

## Interview Tips
- Mention brute force first, then optimize.
- Explain the greedy strategy.

## Common Pitfalls
- Selling before buying.
- Returning negative profit.
- Calling it Two Pointers.

## Personal Notes
- `float('inf')` initializes the running minimum.

## Related Problems
- Best Time to Buy and Sell Stock II
- Best Time to Buy and Sell Stock III
- Maximum Subarray
