'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

'''
logic:
numbers are in ascending order
so get the numbers count and middle value
then find (a[x][y]) x and y value to compare with target
x=middle value row  middle value // len(row)
y=middle value x row index middle value % len(row)

apply binary search
'''

from ast import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mi=(l+r)//2
            mid_val=matrix[mi//n][mi%n]
            if mid_val==target:
                return True
            elif mid_val<target:
                l=mi+1
            else:
                r=mi-1
        return False