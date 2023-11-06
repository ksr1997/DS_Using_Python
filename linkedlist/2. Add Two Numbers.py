'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

'''
logic:
add list wise and take care of the remainder
'''

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=tail=ListNode()
        remain=0

        while l1 or l2:
            if l1 and l2:
                s=l1.val+l2.val+remain
                tail.next=ListNode(s%10)
                remain=s//10
                tail,l1,l2=tail.next,l1.next,l2.next
            elif l1:
                s=l1.val+remain
                tail.next=ListNode(s%10)
                remain=s//10
                tail,l1=tail.next,l1.next
            
            elif l2:
                s=l2.val+remain
                tail.next=ListNode(s%10)
                remain=s//10
                tail,l2=tail.next,l2.next

        if remain:
            tail.next=ListNode(remain)
        
        return head.next



