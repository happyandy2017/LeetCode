'''
Daily Temperatures
  Go to Discuss
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''
class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        '''
           --
         ------
        ---------
        '''
        if not T:
            return T
        
        stack = [] # store element, bottom->top: large->small, each time comes new element, it will push down the stack, pop small one, until it meets bigger one
        result = [0]*len(T)
        for cur_idx, cur_temp in enumerate(T): # for each element in T
            while stack and (cur_temp>stack[-1][1]): # if cur_temp > samll_temp
                small_idx, small_temp = stack.pop() # pop small one
                result[small_idx] = cur_idx-small_idx # update small one's result
            stack.append((cur_idx, cur_temp)) # push big one
        return result
    
# class Solution(object):

#     def dailyTemperatures(self, temps):
        
#         if not temps:
#             return []
        
#         result = [0] * len(temps)
#         stack = []
        
#         for curr_idx, curr_temp in enumerate(temps):
            
#             while stack and curr_temp > stack[-1][1]:
                
#                 last_idx, last_temp = stack.pop()
#                 result[last_idx] = curr_idx - last_idx

#             stack.append((curr_idx, curr_temp))
            
#         return result
    
    def dailyTemperatures2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return T
        
        result = []
        for i in range(len(T)): # for each element in T
            cur = T[i]
            count = 0
            warmer_tem_found = False
            for next in T[i+1:]:
                count += 1
                if next > cur:
                    warmer_tem_found = True
                    result.append(count)
                    break
            if not warmer_tem_found:
                result.append(0)
        return result