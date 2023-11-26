#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ####### Solutions 1 #######
        # output_set = set()
        
        # for bit_subset in range(2**len(nums)):
        #     subset = []
        #     for i in range(len(nums)):
        #         if (1 << i) & bit_subset != 0:
        #             subset.append(nums[i])
            
        #     subset = tuple(sorted(subset))
        #     if subset not in output_set:
        #         output_set.add(subset)
            
        
        # output_list = list(output_set)
        # for i in range(len(output_list)):
        #     output_list[i] = list(output_list[i])
        
        # return output_list
        
        
        ####### Solutions 2 #######
        nums = sorted(nums)
        output_list = []
        
        def dfs(subset, left_set):
            output_list.append(subset)
            
            if len(left_set) == 0:
                return
            
            for i in range(len(left_set)):
                if i > 0 and left_set[i] == left_set[i-1]:
                    continue
                else:
                    dfs(subset + [left_set[i]], left_set[i+1:])
        
        dfs([], nums)
        
        return output_list
# @lc code=end

