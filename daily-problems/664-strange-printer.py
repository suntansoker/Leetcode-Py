'''
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def findTurns(i, j):
            if i == j:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            mn = 10 ** 20
            for k in range(i, j):
                val = findTurns(i, k) + findTurns(k+1, j)
                if s[i] == s[k+1]:
                    val -= 1
                mn = min(mn, val)
            dp[i][j] = mn
            return dp[i][j]
        return findTurns(0, n-1)
