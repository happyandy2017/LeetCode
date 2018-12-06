class Solution:
    def is_not_empty(self, matrix):
        return matrix and matrix[0]
    
    def add(self, result, items):
        for item in items:
            result.append(item)
            
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # check m!=0 or n!=0
        if not self.is_not_empty(matrix):
            return []
        
        result = []
        while matrix:
            # handle first row
            self.add(result, matrix.pop(0))
            
            # handle the last column
            if self.is_not_empty(matrix):
                for row in matrix:
                    result.append(row.pop())
                    
            # handle last row
            if self.is_not_empty(matrix):
                self.add(result, matrix.pop()[::-1]) # pop and reverse last row
                
            # handle first column
            if self.is_not_empty(matrix):
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result