'''
Given an integer array nums of unique elements, return all possible subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
'''

'''
logic:
nums = [1,2,3]
res=[]
for each level, call function with adding nums[i],without adding nums[i]
break when i==len(nums)
                                         [0,[]]
                     [1,[1]],                               [1,[]]
        [2,[1,2]],             [2,[1]],           [2,[2]],           [2,[]]
[3,[1,2,3]], [3,[1,2]], [3,[1,3]], [3,[1]], [3,[2,3]], [3,[2]], [3,[3]], [3,[]]
'''

from ast import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def backtrack(i,sub):
            if i>=len(nums):
                res.append(sub)
                return 
            backtrack(i+1,sub+[nums[i]])
            backtrack(i+1,sub)

        backtrack(0,[])
        return res