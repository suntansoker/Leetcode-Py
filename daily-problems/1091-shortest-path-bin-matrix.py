'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[-1, -1], [-1, 0], [-1, 1],
                      [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        n = len(grid)
        q = []
        if grid[0][0] == 1:
            return -1
        q.append((1, 0, 0))
        vis = set()
        vis.add((0, 0))
        while q:
            dist, x, y = q.pop(0)
            if x == n-1 and y == n-1:
                return dist
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and grid[nx][ny] == 0 and (nx, ny) not in vis:
                    q.append((dist+1, nx, ny))
                    vis.add((nx, ny))
        return -1
