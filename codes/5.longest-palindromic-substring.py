#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
from itertools import combinations

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for left, right in combinations(range(len(s)+1), 2):
            if s[left] == s[right-1] and s[left:right] == s[left:right][::-1]:
                longest = max(longest, s[left:right], key=len)
        
        return longest
        
        
            
# @lc code=end

