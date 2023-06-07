'''
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
'''


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aBin = bin(a)[2:]
        bBin = bin(b)[2:]
        cBin = bin(c)[2:]
        lenA = len(aBin)
        lenB = len(bBin)
        lenC = len(cBin)
        digMax = max(lenA, lenB, lenC)

        aBin = (digMax - lenA) * '0' + aBin
        bBin = (digMax - lenB) * '0' + bBin
        cBin = (digMax - lenC) * '0' + cBin

        count = 0

        for i in range(digMax):
            if cBin[i] == '0':
                if aBin[i] == '1':
                    count += 1
                if bBin[i] == '1':
                    count += 1
            else:
                if aBin[i] == '1' or bBin[i] == '1':
                    continue
                else:
                    count += 1

        return count
