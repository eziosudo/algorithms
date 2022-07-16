# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays. 
# 
#  The overall run time complexity should be O(log (m+n)). 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#  
# 
#  
#  Constraints: 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
#  Related Topics Array Binary Search Divide and Conquer 👍 17728 👎 2108


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length == 1:
            return nums1[0] if len(nums1) == 1 else nums2[0]
        nums = [0] * length
        index, i, j = 0, 0, 0
        for index in range(length):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    nums[index] = nums1[i]
                    i += 1
                else:
                    nums[index] = nums2[j]
                    j += 1
            else:
                break
        while i < len(nums1):
            nums[index] = nums1[i]
            i += 1
            index += 1
        while j < len(nums2):
            nums[index] = nums2[j]
            j += 1
            index += 1

        if length % 2 != 0:
            return nums[length // 2]
        else:
            return (nums[length // 2 - 1] + nums[length // 2]) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        ans = length // 2
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = nums2, nums1
        i = len(A) // 2

        while True:
            Aleft = A[i-1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            j = ans - i
            Bleft = B[j-1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if length % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1


# leetcode submit region end(Prohibit modification and deletion)

s = Solution2()
print(s.findMedianSortedArrays([1, 3, 5], [2, 4]))
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 3], [2, 4]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([0], [0]))
