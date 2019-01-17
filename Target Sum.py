'''
Target Sum
  Go to Discuss
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # dynamic program
        if not nums:
            return 0
        dict = {0:1}
        for i in range(len(nums)):
            # tdict = {}
            import collections
            tdict = collections.defaultdict(int)
            for sum in dict: # 把相同的sum key的merge起来
                # tdict[nums[i]+sum] = tdict.get(nums[i]+sum,0)+dict.get(sum,0)
                # tdict[-nums[i]+sum] = tdict.get(-nums[i]+sum,0)+dict.get(sum,0)
                tdict[sum+nums[i]] += dict[sum]
                tdict[sum-nums[i]] += dict[sum]
            dict = tdict
        return dict.get(S,0)

    # def findTargetSumWays_time_limit_exceed(self, nums, S):
    #     """
    #     :type nums: List[int]
    #     :type S: int
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     if len(nums)==1:
    #         if nums [0]== 0 and S == 0: # important, +-0 = 0, two ways
    #             return 2
    #         if nums[0]==S or -nums[0]==S:
    #             return 1
    #         return 0
    #     return self.findTargetSumWays(nums[1:], S-nums[0]) + self.findTargetSumWays(nums[1:], S+nums[0])
        