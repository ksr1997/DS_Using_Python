'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]
'''

'''
logic: loop through list,sort string using sorted, create dict, and add
'''

from ast import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for string in strs:
            sorted_str=''.join(sorted(string))
            if sorted_str not in d:
                d[sorted_str]=[]
            d[sorted_str].append(string)
        return list(d.values())