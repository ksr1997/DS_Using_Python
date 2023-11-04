'''
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
'''

'''
logic:
backtracking
condition:
len(string)==n*2,then add
left<n
s+'(',left+1,right
right<left
s+')',left,right+1
'''

from ast import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        result = []
        backtrack("", 0, 0)
        return result