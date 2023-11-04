'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

'''

'''
logic:
create dict
find the count of each element by using d.get(i,0)+1
check dict==dict
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dic(string):
            d={}
            for i in string:
                d[i]=d.get(i,0)+1
            return d
        return dic(s)==dic(t)



