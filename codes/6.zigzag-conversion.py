#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        output = ""
        for i in range(numRows):
            index = i
            while index < len(s):
                output += s[index]
                
                if i != 0 and i != numRows - 1:
                    middle_index = index + numRows - (i + 1) + (numRows - 2) - (i - 1)
                    if middle_index < len(s):
                        output += s[middle_index]
                index += numRows * 2 - 2
                
        return output
# @lc code=end

