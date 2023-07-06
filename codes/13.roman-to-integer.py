#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        loma_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        total_num = 0
        
        ex = 0
        for num in s:
            x = loma_dict[num]
            if x <= ex:
                total_num += ex
            else:
                total_num -= ex
            ex = x
        total_num += ex

        return total_num
        
# @lc code=end

