class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        area_l = 0
        area_r = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                area_l += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                area_r += max_r - height[r]
        return area_l + area_r

        
        