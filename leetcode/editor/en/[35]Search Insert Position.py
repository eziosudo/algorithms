# Given a sorted array of distinct integers and a target value, return the 
# index if the target is found. If not, return the index where it would be if it were 
# inserted in order. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums contains distinct values sorted in ascending order. 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics Array Binary Search 👍 8538 👎 434


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start if nums[start] >= target else start + 1


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
