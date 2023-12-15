#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def __init__(self,):
        self.chr_a = ord('a')
        self.num_set = None
        
    def recursive_comb(self, index, output):
            if index >= len(self.num_set):
                return output
            
            num = self.num_set[index]
            flag = 0
            if num > 7:
                flag = 1
            str_list = [chr(self.chr_a + (num - 2) * 3 + s + flag) for s in range(3)]
            if num == 7:
                str_list.append("s")
            elif num == 9:
                str_list.append("z")
            
            temp = []
            for _ in range(len(str_list)):
                temp.append(output.copy())
            
            output = temp
            for i, s in enumerate(str_list):
                for j in range(len(output[i])):
                    output[i][j] += s
            
            temp = []
            for out in output:
                temp.extend(out)
            output = temp

            return self.recursive_comb(index+1, output)
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.num_set = list(map(int, list(digits)))
        if len(digits) == 0:
            return []    
        
        output = [""]
        
        output = self.recursive_comb(0, output)
        return output
# @lc code=end

