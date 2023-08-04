'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

# O(n^2) time complexity

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         st = set(wordDict)

#         dp = [None for _ in range(n+1)]
#         def findCount(start):
#             if start==n:
#                 return True

#             if dp[start] != None:
#                 return dp[start]


#             ans = False
#             for i in range(start+1, n+1):
#                 if s[start:i] in st:
#                     val = findCount(i)
#                     ans = ans or val

#             dp[start] = ans
#             return dp[start]

#         return findCount(0)

# O(n * m * k) time complexity
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        st = set(wordDict)

        dp = [None for _ in range(n+1)]

        def findCount(start):
            if start == n:
                return True

            if dp[start] != None:
                return dp[start]

            ans = False
            for w in wordDict:
                if s[start:].startswith(w):
                    val = findCount(start + len(w))
                    ans = ans or val

            dp[start] = ans
            return dp[start]

        return findCount(0)
