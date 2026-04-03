class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            try:
                hash[i] += 1
                return True
            except:
                hash[i] = 1
        return False