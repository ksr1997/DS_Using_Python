'''
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
'''

'''
logic:
[1,2,3]
iterate through all the numbers and backtrack
1                                                2                  3
append 2[1,2],pop 2 and append 3[1,3]      [2,1],[2,3]       [3,1],[3,2]
[1,2,3],[1,3,2]                           [2,1,3],[2,3,1]   [3,1,2],[3,2,1]
'''

from ast import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in nums:
                if i not in used:
                    used.add(i)
                    path.append(i)
                    backtrack(path, used)
                    path.pop()
                    used.remove(i)

        backtrack([], set())
        return res

