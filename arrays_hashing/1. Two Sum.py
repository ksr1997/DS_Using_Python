'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

'''
logic:
iterate through numbers,
create dict of number,index
check target-number in dict
else add to dict
'''

from ast import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,value in enumerate(nums):
            a=target-value
            if a in seen:
                return [index,seen[a]]
            seen[value]=index