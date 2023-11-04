'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true
'''

'''
logic:
create dict
iterate through loop
check in keys and add to list
else pop element and compare
'''

class Solution:
    def isValid(self, s: str) -> bool:
        d={"(":")","[":"]","{":"}"}
        l=[]
        for i in s:
            if i in d:
                l.append(i)
            elif len(l)==0 or d[l.pop()]!=i:
                return False
        return len(l)==0