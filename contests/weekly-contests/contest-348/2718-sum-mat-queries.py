'''
You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].

Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:

if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.

 

Example 1:


Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
Output: 23
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23. 
Example 2:


Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
Output: 17
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.
 

Constraints:

1 <= n <= 10^4
1 <= queries.length <= 5 * 10^4
queries[i].length == 3
0 <= typei <= 1
0 <= indexi < n
0 <= vali <= 10^5
'''


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row = set()
        col = set()
        sm = 0
        for i in range(len(queries) - 1, -1, -1):
            t = queries[i][0]
            idx = queries[i][1]
            val = queries[i][2]

            count = n
            if t == 0:
                if idx in row:
                    continue
                else:
                    c = len(col)
                    sm += (count - c) * val
                row.add(idx)
            else:
                if idx in col:
                    continue
                else:
                    r = len(row)
                    sm += (count - r) * val
                col.add(idx)

        return sm
