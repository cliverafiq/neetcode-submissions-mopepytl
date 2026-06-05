class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}
        i = 0

        for num in nums:
            if (target-num) in store.keys():
                return [store.get(target-num), i]
            else:
                store[num] = i
            i = i + 1
        
        return