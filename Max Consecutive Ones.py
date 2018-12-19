""" Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000 """

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        
        # find index of 0
        zero_indexs = [-1]    
        for i in range(n):
            if nums[i] == 0:
                zero_indexs.append(i)
        zero_indexs.append(n)
        
        # substract index to get length
        result = -1
        for i in range(len(zero_indexs))[1:]:
            length = zero_indexs[i]-zero_indexs[i-1]-1
            if length > result:
                result = length
        # return the maximum one
        return result
        