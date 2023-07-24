'''
Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.
 

Constraints:

1 <= n <= 300
1 <= x <= 5
'''


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = int(1e9+7)
        # dp = {}

        @cache
        def findWays(no, base):
            val = no - base ** x
            if no == 0:
                return 1
            elif base > n or no < 0 or val < 0:
                return 0
            else:
                take, notTake = 0, 0
                take = findWays(val, base+1)
                notTake = findWays(no, base+1)

                return (take + notTake)

        return findWays(n, 1) % MOD
