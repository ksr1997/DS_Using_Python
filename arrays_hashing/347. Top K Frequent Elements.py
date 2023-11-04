'''
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
'''

'''
logic:
each value count using d.get(i,0)
sort dict by values
'''

from ast import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        sorted_d=dict(sorted(d.items(),key=lambda i:i[1],reverse=True))
        return list(sorted_d.keys())[:k]