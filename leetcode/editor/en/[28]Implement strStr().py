# Implement strStr(). 
# 
#  Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great 
# question to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty 
# string. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "hello", needle = "ll"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
#  Related Topics Two Pointers String String Matching 👍 4470 👎 3778


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if i + len(needle) <= len(haystack) and haystack[i:i + len(needle)] == needle:
                return i
        return -1


# leetcode submit region end(Prohibit modification and deletion)

e = Solution()
print(e.strStr("abcde", "cde"))
