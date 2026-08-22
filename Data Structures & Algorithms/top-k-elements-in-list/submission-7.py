import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] = freq[num] + 1
        out = [0] * k
        for i in range(k):
            out[i] = max(freq, key=freq.get)
            freq[out[i]] = 0
        return out


        