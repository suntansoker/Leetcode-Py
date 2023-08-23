'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
'''


class Solution:
    def convertToTitle(self, colNo: int) -> str:
        ans = ""

        while colNo > 0:
            rem = colNo % 26
            if rem == 0:
                rem = 26

            ch = chr(ord('A') + rem-1)

            colNo -= rem
            colNo = colNo // 26
            ans += ch

        return ans[::-1]
