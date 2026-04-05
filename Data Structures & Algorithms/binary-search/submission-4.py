class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (r+l)//2
        while l < r and nums[m] != target:
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
            m = (r+l)//2
        return m if nums[m] == target else -1