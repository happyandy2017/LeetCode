class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        M = len(matrix)
        if M==0: return []
    
        N = len(matrix[0])
        if N==0: return []

        result = []
        
        # 1. generate segments
        segments = []
        for i in range(M):
            segments.append(self.generate_segment(i, 0, N, matrix))
        
        for j in range(1, N):
            segments.append(self.generate_segment(M-1, j, N, matrix))
        
        # 2. append segments, need to reverse for even one
        i = 1
        for segment in segments:
            # 2.1 if even one, reverse first
            if i%2 == 0:
                segment.reverse()
            
            # 2.2 append all data from segment to result
            for data in segment:
                result.append(data)
                
            i += 1
                
        return result
    
    
    def generate_segment(self, i, j, N, matrix):
        segment = []
        
        while i>=0 and j<N:
            segment.append(matrix[i][j])
            i -= 1
            j += 1
            
        return segment
