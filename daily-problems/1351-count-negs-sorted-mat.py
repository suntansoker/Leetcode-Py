'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
'''


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # BINARY SEARCH
        # ans = 0
        # for i in range(m):
        #     subAns = n
        #     left, right = 0, n-1
        #     while(left<=right):
        #         mid = (left + right) // 2
        #         if grid[i][mid] < 0:
        #             subAns = mid
        #             right = mid - 1
        #         else:
        #             left = mid + 1

        #     ans += (n- subAns)

        # return ans

        # Linear traversal O(m+n)
        colNo = n
        ans = 0
        for row in range(m):
            for j in range(colNo-1, -1, -1):
                if grid[row][j] < 0:
                    colNo = j

            ans += (n-colNo)

        return ans
