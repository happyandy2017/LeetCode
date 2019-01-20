'''
01 Matrix
  Go to Discuss
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(matrix), len(matrix[0])
        def neighbors(i, j):           
            if i+1 < R:     yield i+1, j
            if i-1 >= 0:    yield i-1, j
            if j+1 < C:     yield i, j+1
            if j-1 >= 0:    yield i, j-1
        from collections import deque
        q = deque([(r, c), 0] for r in range(R) for c in range(C) if matrix[r][c] == 0)
        seen = {x for x, _ in q}
        # ans = [[0]*C for _ in matrix]
        while q:
            (r, c), depth = q.popleft()
            matrix[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth+1))
        return matrix
    
class Solution2:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def get_neighbours(i, j):           
            R = len(matrix)
            C = len(matrix[i])
            if i+1 < R:
                yield (i+1, j)
            if i-1 >= 0:
                yield (i-1, j)
            if j+1 < C:
                yield (i, j+1)
            if j-1 >= 0:
                yield (i, j-1)
                
        from collections import deque
        def findNearestPath(i, j):
            step = -1
            visited = set([(i, j)])
            q = deque([(i, j)])
            while q:
                step += 1
                for k in range(len(q)): # FIFO
                    r, c = q.popleft()
                    if matrix[r][c] == 0:
                        return step
                    for n_i, n_j in get_neighbours(r, c):
                        if (n_i, n_j) not in visited:
                            visited.add((n_i, n_j))
                            q.append((n_i, n_j))                            
            return 0
        
        if not matrix:
            return matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = findNearestPath(i, j)
        return matrix

result = Solution().updateMatrix([[1,1,1], [0, 1, 1]])
print(result)