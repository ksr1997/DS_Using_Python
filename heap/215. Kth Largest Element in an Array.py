'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

'''
Only min heap is implemented in python, so need to convert to max heap by 
converting positive values to negative values and applying min heap
import heapq
nums = [3,2,1,5,6,4]
k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
nums=[-i for i in nums]
heapq.heapify(nums)
print(nums)
for i in range(k-1):
    heapq.heappop(nums)
    print("nums after deleting ",nums)  
'''
from ast import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-i for i in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -1*nums[0]
