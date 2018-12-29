
class Solution:
    def quicksort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [2,1,3,5,4,6]
        N=len(nums)
        for i in range(N-1):
            for j in range(N-2-i+1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        

nums1=[4,3,2,2,4,6,8,9,0,2,4,1]
Solution().quicksort(nums1)
for num in nums1:
    print(num)