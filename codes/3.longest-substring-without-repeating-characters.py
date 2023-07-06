#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        char_set = {}
        left = 0
        
        for i, letter in enumerate(s):
            index = char_set.get(letter)
            if index is not None and index >= left:
                left = index+1
            char_set[letter] = i
            output = max(output, i - left + 1)
        
        return output
        
# @lc code=end

