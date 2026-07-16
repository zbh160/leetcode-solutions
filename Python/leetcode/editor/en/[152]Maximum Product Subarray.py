# Given an integer array nums, find a subarray that has the largest product, 
# and return the product. 
# 
#  The test cases are generated so that the answer will fit in a 32-bit integer.
#  
# 
#  Note that the product of an array with a single element is the value of that 
# element. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
#  
#  
# 
#  Related Topics Array Dynamic Programming 👍 20659 👎 835


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # min_product * neg could be new current_max
        # max could be nums[i], previous_max * nums[i], current_min * nums[i]
        # min could be nums[i], previous_max * nums[i], current_min * nums[i]
        current_min = nums[0]
        current_max = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            previous_max = current_max
            current_max = max(nums[i], previous_max * nums[i], current_min * nums[i])
            current_min = min(nums[i], previous_max * nums[i], current_min * nums[i])
            max_product = max(max_product, current_max)
        return max_product

# leetcode submit region end(Prohibit modification and deletion)
