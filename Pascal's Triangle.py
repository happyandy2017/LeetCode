class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1: 
            return [[1]]
        if numRows==2: 
            return [[1],[1, 1]]
        
        # get results of numRows-1
        pre_result = self.generate(numRows-1)
        
        # get current row
        pre_row = pre_result[-1]
        current_row = []
        for i in range(numRows):
            if i in [0, numRows-1]:
                current_row.append(1)
                continue
            
            current_row.append(pre_row[i-1]+pre_row[i])
        
        pre_result.append(current_row)
        return pre_result

Solution().generate(5)