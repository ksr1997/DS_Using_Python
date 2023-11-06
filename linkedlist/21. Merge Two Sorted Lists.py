'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []
'''

'''
point the list with two pointers
first element from both lists, compare and add to one pointer,
one pointer iterate through the end, return another pointer
'''

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = merger = ListNode()
        
        # Choose smallest each time
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    merger.next = list1
                    list1 = list1.next
                else:
                    merger.next = list2
                    list2 = list2.next
            elif list1:
                merger.next = list1
                list1 = list1.next
                
            elif list2:
                merger.next = list2
                list2 = list2.next
                
            merger = merger.next
     
        return head.next