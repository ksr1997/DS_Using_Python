'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. 
The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.
'''

'''
Need to Know:
# Implements Min Heap Property
import heapq
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
# li = [1, 3, 9, 7, 5]
heapq.heappush(li, 4)
# li = [1, 3, 4, 9, 7, 5]
heapq.heappop(li)
# 1
li1 = [5, 2, 9, 4, 3]
li2 = [5, 2, 9, 4, 3]
heapq.heappushpop(li1, 1)
#first push and then pop min element
heapq.heapreplace(li2, 1)
#first pop and then push into list

Logic:
As min heap is available, apply - sign to the elements and apply the above functions
'''

from ast import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if first<second:
                heapq.heappush(stones,first-second)
        stones.append(0)
        return stones[0]