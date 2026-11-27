class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        found = {}

        for i, num in enumerate(nums):
            if not(target - num) in found.keys():
                found[num] = i
            else:
                break
        return [found[target - num], i]

