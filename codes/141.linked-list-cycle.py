#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


### Solution 1: Hash Table
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         point_set = set()
        
#         while head:
#             if head in point_set:
#                 return True
#             else:
#                 point_set.add(head)
#                 head = head.next

### Solution 2: Tortoise and Hare
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_move = head
        slow_move = head
        
        while fast_move and fast_move.next:
            fast_move = fast_move.next.next
            slow_move = slow_move.next
            
            if fast_move == slow_move:
                return True

        return False
                
                
            

            
# @lc code=end

