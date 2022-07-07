# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 👍 13992 👎 652


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if len(stack) == 0 or s[i] in map.values():
                stack.append(s[i])
            elif map[s[i]] != stack.pop():
                return False
        return True if len(stack) == 0 else False


# leetcode submit region end(Prohibit modification and deletion)

e = Solution()
print(e.isValid('()'))
print(e.isValid("()[]{}"))
print(e.isValid('(['))
print(e.isValid('([])'))
print(e.isValid('([{])'))

