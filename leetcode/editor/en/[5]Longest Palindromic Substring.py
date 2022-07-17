# Given a string s, return the longest palindromic substring in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: "bb"
#  
# 
#  
#  Constraints:

# 
#  
#  1 <= s.length <= 1000 
#  s consist of only digits and English letters. 
#  
#  Related Topics String Dynamic Programming 👍 19755 👎 1143


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = s
        length = 1
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                dp[i][j] = True if i == j else False
        i = len(s) - 2
        j = len(s) - 1
        while i >= 0 and j >= 0:
            while j > i:
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    length = max(length, j - i)
                    ss = s[i:j+1] if j - i == length else ss
                j -= 1
            i -= 1
            j = len(s) - 1
        return ss

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
# print(s.longestPalindrome("abcba"))
# print(s.longestPalindrome("abcbd"))
# print(s.longestPalindrome("a"))
print(s.longestPalindrome("cbbd"))
