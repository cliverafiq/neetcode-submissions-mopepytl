class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        vals = 1
        for i, val in enumerate(nums):
            output.append(vals)
            vals = vals * val

        vals = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] = output[j] * vals
            vals = vals * nums[j]
        
        return output
