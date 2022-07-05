# Given an integer x, return true if x is palindrome integer. 
# 
#  An integer is a palindrome when it reads the same backward as forward. 
# 
#  
#  For example, 121 is a palindrome while 123 is not. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#  
# 
#  Example 2: 
# 
#  
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it 
# becomes 121-. Therefore it is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without converting the integer to a string? 
# Related Topics Math 👍 6254 👎 2191


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        s = str(x)
        start = 0
        end = len(s) - 1
        while s[start] == s[end] and start < end:
            start += 1
            end -= 1
        if start == end or end == start - 1:
            return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        # 反转字符串，这也太方便了吧···
        r = s[::-1]
        return s == r


# leetcode submit region end(Prohibit modification and deletion)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        mid = len(str(x)) // 2
        if len(str(x)) % 2 == 0:
            return True if str(x)[:mid] == str(x)[mid:][::-1] else False
        else:
            return True if str(x)[:mid] ==str(x)[mid+1:][::-1] else False

# leetcode submit region end(Prohibit modification and deletion)


e = Solution3()
print(e.isPalindrome(1234))
print(e.isPalindrome(121))
print(e.isPalindrome(0))
print(e.isPalindrome(22))
print(e.isPalindrome(-100))
print(e.isPalindrome(111))
