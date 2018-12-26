# Rotate Array
#   Go to Discuss
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k%N
        if N==1 or k==0:
            return
        
        nums[:] = nums[-k:]+nums[:-k]
        
    def rotate_2(self, nums, k):
        N = len(nums)
        k = k%N
        if N==1 or k==0:
            return


        l=0 # number of swaps
        
        i=0
        j=(i+k)%N
        while l<N-1:
            if i == j:
                i+=1
                j=(i+k)%N
                
                l+=1 # need to reduce by 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j= (j+k)%N
            
            l+=1

                

        
                
        # for j in range(k):
        #     temp = nums[N-1]
        #     for i in range(N-2,-1, -1):
        #         nums[i+1]=nums[i]
        #     nums[0] = temp
        # count = 0
        # i = 0
        # while count<N:
        #     i_next = i+k
        #     if i_next>=N:
        #         i_next = i_next%N
        #         temp = nums[i_next]
        #         nums[i_next]=nums[i]
        #         i=i_next+1
        #     else:
        #         temp = nums[i_next]
        #         nums[i_next]=nums[i]
        #         i=i_next
        #     count+=1
        
        # return nums

time1 = time.time()

nums = [1,2,3,4,5,6]
k = 6
Solution().rotate(nums, k)
print(nums)

print('time', time.time()-time1)
