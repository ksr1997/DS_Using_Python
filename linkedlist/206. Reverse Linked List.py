'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]
'''

'''
logic:
point to the starting node, reverese it
iterate through the first node, make second node as first like wise...
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node=head
        new_list=None
        while current_node:
            next_node=current_node.next
            current_node.next=new_list
            new_list=current_node
            current_node=next_node
        return new_list