#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
class Solution:
    def __init__(self):
        self.total_time = 0
        self.current_char = 'a'
    
    def min_diff_char(self, target_char: str) -> int:
        length = abs(ord(self.current_char) - ord(target_char))
        return min(length, 26 - length)
    
    def move_pointer(self, target_char: str) -> None:
        if self.current_char == target_char:
            return 
        
        self.total_time += self.min_diff_char(target_char)
    
    def type_char(self, current_char: str) -> int:
        self.total_time += 1
        self.current_char = current_char
    
    def minTimeToType(self, word: str) -> int:
        for char in word:
            self.move_pointer(char)
            self.type_char(char)
        
        return self.total_time
        
# @lc code=end

