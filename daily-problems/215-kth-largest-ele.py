class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(len(nums)):
            heapq.heappush(arr, -nums[i])

        while k > 0:
            ele = -heapq.heappop(arr)
            k -= 1

        return ele
