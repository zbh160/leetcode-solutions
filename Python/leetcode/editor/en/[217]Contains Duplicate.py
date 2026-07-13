# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [1,2,3,1] 
#  
# 
#  Output: true 
# 
#  Explanation: 
# 
#  The element 1 occurs at the indices 0 and 3. 
# 
#  Example 2: 
# 
#  
#  Input: nums = [1,2,3,4] 
#  
# 
#  Output: false 
# 
#  Explanation: 
# 
#  All elements are distinct. 
# 
#  Example 3: 
# 
#  
#  Input: nums = [1,1,1,3,3,4,3,2,4,2] 
#  
# 
#  Output: true 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics Array Hash Table Sorting 👍 14088 👎 1373


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_show = set()
        for num in nums:
            if num in num_show:
                return True
            num_show.add(num)
        return False

# leetcode submit region end(Prohibit modification and deletion)
