'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''

'''
logic:
iterate through all the elements and backtrack it.
for removing duplicates, use append and pop
sort the elements and move to next element if already seen
'''


from ast import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(nums,target,li,res):
            if target==0:
                res.append(li[:])
                return
            if target<0:
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                li.append(nums[i])
                dfs(nums[i+1:],target-nums[i],li,res)
                li.pop()
        candidates.sort()
        dfs(candidates,target,[],res)
        return res
            