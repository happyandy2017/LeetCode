# Pascal's Triangle II
#   Go to Discuss
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex<=0:
            return [1]

        pre_row = [1]
        for i in range(1, rowIndex+1):
            current_row = [1]*(i+1)
            for j in range(1, i):
                current_row[j]=pre_row[j-1]+pre_row[j]
            pre_row = current_row
        return current_row
    
    def getRow2(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0: 
            return [1]
        if rowIndex==1: 
            return [1, 1]

        # get results of numRows-1
        pre_row = self.getRow(rowIndex-1)

        # get current row
        current_row = []
        for i in range(rowIndex+1):
            if i in [0, rowIndex]:
                current_row.append(1)
                continue

            current_row.append(pre_row[i-1]+pre_row[i])

        return current_row