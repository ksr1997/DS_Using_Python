'''
Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3
'''

'''
logic:
floyd tortoise and hare problem
first find the common point.
second, distance from the common point and start are both equal. 
return the intersection value which is the duplicate
'''

from ast import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyd tortoise and hare problem
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break     
        start=0
        while True:
            slow=nums[slow]
            start=nums[start]
            if slow==start:
                return slow