'''
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
 

Constraints:

0 <= k < n <= goal <= 100
'''


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[-1 for _ in range(n + 1)] for _ in range(goal + 1)]

        def findPlaylists(g, l):
            if l == 0 and g == 0:
                return 1
            if l == 0 or g == 0:
                return 0

            if dp[g][l] != -1:
                return dp[g][l]

            # new song
            dp[g][l] = ((n-l+1) * findPlaylists(g-1, l-1)) % MOD
            # same song
            if l-k > 0:
                dp[g][l] += ((l-k) * findPlaylists(g-1, l)) % MOD
                dp[g][l] %= MOD

            return dp[g][l]

        return findPlaylists(goal, n)
