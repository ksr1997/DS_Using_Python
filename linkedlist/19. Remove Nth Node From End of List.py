'''
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []
'''

'''
logic:
1,2,3,4,5,6,7,8,9,10

nth number from the last using slow and fast pointers
2 from the end
point head to two pointers
1:one pointer move upto n from start
move upto 2
2: from 2 take first pointer and move to end
here start the second pointer. it will travel upto 8 which is n number from last

once n number from last is found, just remove it using next.next
'''

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        entire=upton=dummy
        for i in range(n+1):
            entire=entire.next
        while entire:
            entire=entire.next
            upton=upton.next
        upton.next=upton.next.next
        return dummy.next