class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heappush(h, -n)
        for i in range(k-1):
            heappop(h)
        return -heappop(h)