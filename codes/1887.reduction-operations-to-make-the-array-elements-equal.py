#
# @lc app=leetcode id=1887 lang=python3
#
# [1887] Reduction Operations to Make the Array Elements Equal
#
from collections import defaultdict

# @lc code=start
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0
        
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
                
        sorted_num_set = sorted(list(num_dict.keys()), reverse=True)
        ex_n = sorted_num_set[0]
        for n in sorted_num_set[1:]:
            ans += num_dict[ex_n]
            num_dict[n] += num_dict[ex_n]
            ex_n = n
        
        return ans
        
# @lc code=end

