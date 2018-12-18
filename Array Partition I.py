class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#Consider the smallest element x. It should be paired with the next smallest element, because min(x, anything) = x, and having bigger elements only helps you have a larger score. Thus, we should pair adjacent elements together in the sorted array.
        return sum(sorted(nums)[::2])
#         result = 0
#         for i in range(len(nums)//2):
#             result+=nums[2*i]
            
#         return result