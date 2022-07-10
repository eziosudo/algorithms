# Given a string s, find the length of the longest substring without repeating 
# characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table String Sliding Window 👍 26179 👎 1139


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in map:
                i = max(map[s[j]], i)
            ans = max(ans, j - i + 1)
            map[s[j]] = j + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("abcabc"))
print(s.lengthOfLongestSubstring("abcdeafdbgcbb"))

