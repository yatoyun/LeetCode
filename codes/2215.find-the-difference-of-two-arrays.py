#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        ######### Solution 1 #########
        intersect_set = set(nums1) & set(nums2)    
        nums1 = set(nums1) - intersect_set
        nums2 = set(nums2) - intersect_set
        return [list(nums1), list(nums2)]
        
        ######### Solution 2 #########
        # a = set(nums1) - set(nums2)
        # b = set(nums2) - set(nums1)
        # return [list(a), list(b)]
# @lc code=end

