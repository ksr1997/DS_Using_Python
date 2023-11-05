'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

'''
logic:
create set
iterate through the string
add to set if i not in set
else:
remove from the start until element is not found
count the removed element. It acts a pointer

count=max(count,index+1-pointer)

pw:
max(0,1+1-0)
pww:
max(2,2+1-2)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=set()
        res=0
        l=0
        for i in range(len(s)):
            while s[i] in unique:
                unique.remove(s[l])
                l=l+1
            unique.add(s[i])
            res=max(res,i+1-l)
        return res