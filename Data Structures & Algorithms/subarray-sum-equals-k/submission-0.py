class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        count = 0
        found = {0 : 1}
        for num in nums:
            currSum += num
            count += found.get(currSum - k, 0)
            found[currSum] = found.get(currSum, 0) + 1
        return count