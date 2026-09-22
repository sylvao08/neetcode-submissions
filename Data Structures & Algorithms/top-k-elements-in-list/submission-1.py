class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop nums:
        num_cnt = {}
        for num in nums:
            num_cnt[num] = num_cnt.get(num, 0) + 1
        # heap
        import heapq
        top_k = []
        for num, cnt in num_cnt.items():
            heapq.heappush(top_k, (cnt, num))
            if len(top_k)>k:
                heapq.heappop(top_k)
        return [num for cnt, num in top_k]
        