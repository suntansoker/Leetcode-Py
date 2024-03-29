'''
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
'''


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]

        def findMin(i, j):
            if i >= n1:
                sm = 0
                for k in range(j, n2):
                    sm += ord(s2[k])
                return sm

            if j >= n2:
                sm = 0
                for k in range(i, n1):
                    sm += ord(s1[k])
                return sm

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            t1, t2 = 0, 0
            if s1[i] == s2[j]:
                ans = findMin(i+1, j+1)
            else:
                t1 = ord(s1[i]) + findMin(i+1, j)
                t2 = ord(s2[j]) + findMin(i, j+1)
                ans = min(t1, t2)

            dp[i][j] = ans
            return dp[i][j]

        return findMin(0, 0)
