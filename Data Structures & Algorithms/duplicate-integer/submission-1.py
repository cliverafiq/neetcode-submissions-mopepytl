class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = {}

        for num in nums:
            if num in found.keys():
                print(num)
                return True
            found[num] = 1
        
        return False
