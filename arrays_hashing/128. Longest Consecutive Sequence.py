'''
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

'''
logic:
set of the elements
pop one element, check num-1,num+1 in list, if yes remove
10
9,11
8,9,11,12
return 12-8+1 or max

use two while loop
one for iteration
another for checking -1,+1
'''

from ast import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        max_length = 0

        while uniques:
            low = high = uniques.pop()
            
            while low - 1 in uniques or high + 1 in uniques:
                if low - 1 in uniques:
                    uniques.remove(low - 1)
                    low -= 1
                
                if high + 1 in uniques:
                    uniques.remove(high + 1)
                    high += 1

            max_length = max(high - low + 1, max_length)

        return max_length
        