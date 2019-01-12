''''
Perfect Squares
  Go to Discuss
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
import queue
import math

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def neighbours(cur):
            for i in range(1, int(math.sqrt(n)+1)):
                if cur + i*i<=n: # importat!!! cut branches
                    yield cur + i*i
                           
        q1 = queue.Queue() # important: no queue.Queue(0), it is wrong
        q1.put(0)
        visited = set([0])
        step = -1
        while not q1.empty():
            step += 1
            size = q1.qsize()
            for i in range(size): # important!!!
                cur = q1.get() # get first node from queue
                if cur == n:
                    return step
                for next in neighbours(cur):
                    if next not in visited: # importat!!! cut branches
                        q1.put(next)
                        visited.add(next)
        return -1

print(Solution().numSquares(13))