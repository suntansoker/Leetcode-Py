'''
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

 

Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
'''


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        ref = 1 << 6
        m = len(grid)
        n = len(grid[0])
        q = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 'a' and grid[i][j] <= 'f':
                    idx = ord(grid[i][j]) - ord('a')
                    ref |= (1 << idx)
                elif grid[i][j] == '@':
                    q.append((0, i, j, 1 << 6))
                    visited.add((i, j, 1 << 6))

        ans = -1
        di = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        while q:
            dist, r, c, pat = q.pop(0)
            if pat == ref:
                ans = dist
                return ans
            for dx, dy in di:
                x = r + dx
                y = c + dy
                if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] != '#' and (x, y, pat) not in visited:
                    if grid[x][y] >= 'a' and grid[x][y] <= 'f':
                        idx = ord(grid[x][y]) - ord('a')
                        newPat = pat | (1 << idx)
                        q.append((dist+1, x, y, newPat))
                        visited.add((x, y, newPat))
                    elif grid[x][y] >= 'A' and grid[x][y] <= 'F':
                        idx = ord(grid[x][y]) - ord('A')
                        val = pat & (1 << idx)
                        if val > 0:
                            q.append((dist+1, x, y, pat))
                            visited.add((x, y, pat))
                    else:
                        q.append((dist+1, x, y, pat))
                        visited.add((x, y, pat))

        return ans
