'''
Koko loves to eat bananas. 
There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30
'''

'''
logic:
piles = [3,6,7,11],h=8
based on example
3/4 + 6/4 + 7/4 + 11/4
=1  +  2  +  2  + 3
<=8 
we have 4 and we got 8.

but how to get 4 and where to start.

binary search, find middle value[(1+max of piles)/2]
do the math and get number of hours,
if no of hours<h
we need to get more hours, so divided by value should be less
new middle value = (1+middle value/2)
caculate until number of hours = h
'''

from ast import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            m=(l+r)//2
            hr=sum([math.ceil(i/m) for i in piles])
            if hr<=h:
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res
