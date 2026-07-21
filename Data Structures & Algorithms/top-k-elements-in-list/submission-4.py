import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i not in freq.keys():
                freq[i] = 1
            else:
                freq[i] = freq[i] + 1
        print (freq)
        sol = []
        for j in range(k):
            high = max(freq, key=freq.get)
            print(freq)
            sol.append(high)
            freq[high] = 0
        return sol
            

        