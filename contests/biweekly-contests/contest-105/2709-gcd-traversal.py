'''
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

 

Example 1:

Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
Example 2:

Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
Example 3:

Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        MAX = max(nums) + 1
        primes = [True] * MAX
        spf = [i for i in range(MAX)]

        def findPrimes():
            primes[0] = primes[1] = False
            i = 2
            while i*i < MAX:
                if primes[i]:
                    for j in range(i*i, MAX, i):
                        if primes[j]:
                            spf[j] = i
                        primes[j] = False
                i += 1

        def findPrimeFactors(num):
            primeFactors = set()
            while num != 1:
                sp = spf[num]
                primeFactors.add(sp)
                num = num // sp

            return list(primeFactors)

        findPrimes()
        n = len(nums)
        mp = defaultdict(list)
        for i in range(n):
            mp[i] = findPrimeFactors(nums[i])

        rmp = defaultdict(list)
        for k, v in mp.items():
            for val in v:
                rmp[val].append(k)

        adjList = defaultdict(list)

        for k in rmp.keys():
            vArray = rmp[k]
            if len(vArray) < 2:
                continue
            for i in range(1, len(vArray)):
                adjList[vArray[i]].append(vArray[i-1])
                adjList[vArray[i-1]].append(vArray[i])

        count = 0
        vis = set()

        def dfs(index):
            nonlocal count
            vis.add(index)
            count += 1
            for it in adjList[index]:
                if it not in vis:
                    dfs(it)

        dfs(0)
        if count == n:
            return True

        return False
