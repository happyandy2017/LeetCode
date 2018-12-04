class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        for num in nums:
            total_sum += num
        
        sum=0
        length = len(nums)
        for i in range(length):
            if sum*2+nums[i] == total_sum:
                return i
            sum = sum + nums[i]
        
        return -1