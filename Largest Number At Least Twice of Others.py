class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. find the largest num: num_largest, index_largest
        num_largest = max(nums)
        index_largest = nums.index(num_largest)

        # num_largest = -1
        # index_largest = -1
        # i = 0
        # for num in nums:
        #     if num > num_largest:
        #         index_largest = i
        #         num_largest = num
                
        #     i += 1

        # 2. iterate nums, check whether num_largest is at least twice as much as every other number in the array
        i = 0
        for num in nums:
            if num == num_largest:
                i += 1
                continue
            
            if num*2 > num_largest:
                return -1
            i += 1
            
        return index_largest

solution = Solution()
print(solution.dominantIndex([0,0,3,2]))