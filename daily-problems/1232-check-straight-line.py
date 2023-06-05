'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
'''


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        fx = coordinates[0][0]
        fy = coordinates[0][1]
        sx = coordinates[1][0]
        sy = coordinates[1][1]
        slope = inf
        if sx-fx != 0:
            slope = (sy-fy)/(sx-fx)

        n = len(coordinates)
        for i in range(2, n):
            ns = inf
            if coordinates[i][0] - coordinates[i-1][0] != 0:
                ns = (coordinates[i][1] - coordinates[i-1][1]) / \
                    (coordinates[i][0] - coordinates[i-1][0])
            if ns != slope:
                return False

        return True
