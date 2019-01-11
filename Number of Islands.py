'''
Number of Islands
  Go to Discuss
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        # Iterate through each of the cell and if it is an island, do dfs to mark all adjacent islands, then increase the counter by 1.
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)                
                    result +=1
        return result
    
    def dfs(self, grid, i, j):
        if (i in range(len(grid))) and (j in range(len(grid[i]))) and grid[i][j]=='1':
            grid[i][j] = '#'
            for (m, n) in zip((i+1, i-1, i, i), (j, j, j+1, j-1)):
                self.dfs(grid, m, n)

    def numIslands_2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        def sink(i, j):
            if (i in range(len(grid))) and (j in range(len(grid[i]))) and grid[i][j]=='1': # string '1'
                grid[i][j] = '0' # string '0'
                for (m, n) in zip((i+1, i-1, i, i), (j, j, j+1, j-1)):
                    sink(m, n)
                return 1
            return 0
        
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[i])): # i not 0
                result.append(sink(i,j))
        return sum(result)

    def numIslands_good(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))) # The map function isn't executed until list is ran on the mapped item. The map function isn't executed until list is ran on the mapped item. https://stackoverflow.com/questions/13623634/python-3-map-function-is-not-calling-up-function
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))