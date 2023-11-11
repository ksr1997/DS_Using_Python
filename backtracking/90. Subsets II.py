'''
Given an integer array nums that may contain duplicates, 
return all possible subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]
'''
'''
logic:
Same as subset, apply condition
'''

from ast import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(count,elements):
            if count==len(nums):
                if elements not in res:
                    res.append(elements)
                return
            dfs(count+1,elements+[nums[count]])
            dfs(count+1,elements)
        
        dfs(0,[])
        return res