"""
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            
    def moveZeroes_0(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N<=1 or 0 not in nums:
            return None
        
        for i in range(N)[::-1]:
            if nums[i]!=0:
                continue
            
            j=i
            while j<N-1 and nums[j+1]!=0:
                temp=nums[j+1]
                nums[j+1]=nums[j]
                nums[j]=temp
                j+=1