'''
Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

'''
logic:
find single zero or multiple zero
***Interesting logic:
single zero and multiple zero
'''

from ast import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        single_zero=False
        multiple_zero=False
        product=1
        for num in nums:
            if single_zero and num==0:
                multiple_zero=True
                break
            if num==0:
                single_zero=True
            else:
                product=product*num
        
        for i in range(len(nums)):
            if multiple_zero:
                nums[i]=0
                continue
            if single_zero:
                if nums[i]==0:
                    nums[i]=product
                else:
                    nums[i]=0
            else:
                nums[i]=product//nums[i]
            
        return nums