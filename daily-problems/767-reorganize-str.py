'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        mp = defaultdict(int)
        mx = 0
        mxEle = ''
        for i in range(n):
            mp[s[i]] += 1
            if mp[s[i]] > mx:
                mx = mp[s[i]]
                mxEle = s[i]

        if mx > (n+1) // 2:
            return ""

        res = [''] * n

        i = 0

        while mp[mxEle] > 0:
            res[i] = mxEle
            mp[mxEle] -= 1
            i += 2

        for key in mp.keys():
            while mp[key] > 0:
                if i >= n:
                    i = 1
                res[i] = key
                mp[key] -= 1
                i += 2

        return ("").join(res)
