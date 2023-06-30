'''
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 

Example 1:


Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:


Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:


Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
 

Constraints:

2 <= row, col <= 2 * 10^4
4 <= row * col <= 2 * 10^4
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.
'''


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = len(cells)
        left, right = 0, n-1
        ans = -1

        def isPossible(mid):
            grid = [[0 for _ in range(col)] for _ in range(row)]
            for i in range(mid+1):
                grid[cells[i][0]-1][cells[i][1]-1] = 1

            di = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            q = []
            vis = set()
            for i in range(col):
                if grid[0][i] == 0:
                    q.append((0, i))
                    vis.add((0, i))

            gotIt = 0
            while q:
                r, c = q.pop()
                if r == row-1:
                    gotIt = 1
                    break
                for dx, dy in di:
                    x = r + dx
                    y = c + dy
                    if x >= 0 and x < row and y >= 0 and y < col and grid[x][y] == 0 and (x, y) not in vis:
                        q.append((x, y))
                        vis.add((x, y))

            return gotIt

        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid) == 1:
                ans = mid+1
                left = mid + 1
            else:
                right = mid - 1

        return ans
