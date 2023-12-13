#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ############# original ############
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     first_node = head
    #     second_node = head
        
    #     diff_first_second = 0
    #     while first_node.next != None:
    #         first_node = first_node.next
            
    #         if diff_first_second == n:
    #             second_node = second_node.next
    #         else:
    #             diff_first_second += 1
        
    #     if diff_first_second == 0:
    #         return None
    #     elif diff_first_second != n:
    #         return head.next
        
    #     second_node.next = second_node.next.next
        
    #     return head
    
    ############ more smart ###########
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        first_node = head
        second_node = dummy
        
        while n > 1:
            first_node = first_node.next
            n -= 1
        
        while first_node.next != None:
            first_node = first_node.next
            second_node = second_node.next
        
        second_node.next = second_node.next.next
        
        return dummy.next
# @lc code=end

