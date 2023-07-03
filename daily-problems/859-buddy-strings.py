'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

Constraints:

1 <= s.length, goal.length <= 2 * 10^4
s and goal consist of lowercase letters.
'''


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0
        first, second = -1, -1
        arr1 = [0] * 26
        arr2 = [0] * 26

        if len(s) != len(goal):
            return False
        for i in range(len(goal)):
            if s[i] != goal[i]:
                count += 1
                if first == -1:
                    first = i
                else:
                    second = i
            arr1[ord(s[i]) - ord('a')] += 1
            arr2[ord(goal[i]) - ord('a')] += 1
        if arr1 != arr2:
            return False
        if count == 2:
            if s[first] == goal[second] and s[second] == goal[first]:
                return True
            else:
                return False
        elif count == 0:
            for i in range(26):
                if arr1[i] > 1:
                    return True
            return False
        return False
