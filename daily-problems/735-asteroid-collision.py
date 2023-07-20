'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pQueue = []
        nQueue = []
        for i in range(len(asteroids)):
            if asteroids[i] >= 0:
                pQueue.append((asteroids[i], i))
            else:
                gone = False
                while len(pQueue) > 0:
                    if pQueue[-1][0] >= abs(asteroids[i]):
                        gone = True
                        if pQueue[-1][0] == abs(asteroids[i]):
                            pQueue.pop()
                        break
                    else:
                        pQueue.pop()
                if not gone:
                    nQueue.append((asteroids[i], i))
        ans = pQueue+nQueue
        ans.sort(key=lambda x: x[1])
        # print(ans)
        res = []
        for a in ans:
            res.append(a[0])

        return res
