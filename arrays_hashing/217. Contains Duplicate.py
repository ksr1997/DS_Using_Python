'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

'''

'''
logic:
create set
new element: add to set,
if duplicate, its already in set, so return true
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(set(nums))!=len(nums)
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            else:
                num_set.add(i)
        return False
