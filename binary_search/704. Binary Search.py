'''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

'''
logic:
check middle index and compare with target
if target less, then end is middle, else start is middle
'''

from ast import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                return m
            elif target<nums[m]:
                h=m-1
            else:
                l=m+1
        return -1