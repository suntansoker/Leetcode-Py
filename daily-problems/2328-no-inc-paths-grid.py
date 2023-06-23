'''
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

 

Example 1:


Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
1 <= grid[i][j] <= 10^5
'''


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10 ** 9 + 7
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        di = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def findPathsDFS(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            dp[r][c] = 1
            for dx, dy in di:
                newR = r + dx
                newC = c + dy
                if newR >= 0 and newR < m and newC >= 0 and newC < n and grid[newR][newC] > grid[r][c]:
                    dp[r][c] += (findPathsDFS(newR, newC)) % MOD
            return dp[r][c] % MOD

        ans = 0
        for i in range(m):
            for j in range(n):
                res = findPathsDFS(i, j)
                ans += res % MOD

        return ans % MOD
