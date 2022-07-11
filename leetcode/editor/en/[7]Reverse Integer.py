# Given a signed 32-bit integer x, return x with its digits reversed. If 
# reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed 
# or unsigned). 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 123
# Output: 321
#  
# 
#  Example 2: 
# 
#  
# Input: x = -123
# Output: -321
#  
# 
#  Example 3: 
# 
#  
# Input: x = 120
# Output: 21
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
#  Related Topics Math 👍 7602 👎 10109


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        def outside(x: int) -> bool:
            if x > 2 ** 31 - 1 or x < -2 ** 31:
                return False

        if outside(x) is False:
            return 0
        positive = True
        if x < 0:
            positive = False
            x = -x
        rx = 0
        while x > 0:
            n = x % 10
            rx = rx * 10 + n
            x //= 10
        if outside(rx) is False:
            return 0
        return rx if positive else -rx


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.reverse(-12345))
print(s.reverse(1534236469))
