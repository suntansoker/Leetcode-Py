'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 10^4
'''


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        m = len(nums1)
        n = len(nums2)
        vis = set()
        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
        vis.add((0, 0))
        ans = []

        while k > 0:
            if len(pq) > 0:
                sm, fIndex, sIndex = heapq.heappop(pq)
                ans.append([nums1[fIndex], nums2[sIndex]])
                if (sIndex+1) < n and (fIndex, sIndex+1) not in vis:
                    new_sm = nums1[fIndex] + nums2[sIndex+1]
                    heapq.heappush(pq, (new_sm, fIndex, sIndex+1))
                    vis.add((fIndex, sIndex+1))
                if (fIndex+1) < m and (fIndex+1, sIndex) not in vis:
                    new_sm = nums1[fIndex+1] + nums2[sIndex]
                    heapq.heappush(pq, (new_sm, fIndex+1, sIndex))
                    vis.add((fIndex+1, sIndex))
            k -= 1

        return ans
