'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []
'''

'''
logic:
nums = [2,3,5], target = 8
for i in range(3):
2,3,5
dfs(nums[0:],8-2,[]+[2])
                                                                    2,                                                                                                                                                                                                                                            3,                                            5
                                                        dfs(nums[0:],8-2-2,[]+[2]+[2])                                                                                                                                                                                                                   dfs(nums[0:],8-2-3,[]+[2]+[3])          dfs(nums[0:],8-2-5,[]+[2]+[5]) 
                                                                  2,3,5
                                            dfs(nums[0:],8-2-2-2,[]+[2]+[2]+[2]),                                                                              dfs(nums[1:],8-2-2-3,[]+[2]+[2]+[3]),                                           dfs(nums[2:],8-2-2-5,[]+[2]+[2]+[5])
                  2,                                         3,                                            5                                                    3                                         5
dfs(nums[0:],8-2-2-2-2,[]+[2]+[2]+[2]+[2]), dfs(nums[1:],8-2-2-2-3,[]+[2]+[2]+[2]+[3]), dfs(nums[2:],8-2-2-2-5,[]+[2]+[2]+[2]+[5])   ||     dfs(nums[1:],8-2-2-3-3,[]+[2]+[2]+[3]+[3]), dfs(nums[1:],8-2-2-3-5,[]+[2]+[2]+[3]+[5]),
looping through the entire set multiple times until condition is met.
condition is target<0 or target==0

'''

from ast import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums,target,path,res):
            if target<0:
                return 
            if target==0:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i:],target-nums[i],path+[nums[i]],res)
        
        res=[]
        dfs(candidates,target,[],res)
        return res