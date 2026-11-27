class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = -1
        found = {}
        best = 0
        for r, ch in enumerate(s):
            if ch in found and found[ch] >= l:
                l = found[ch]
            found[ch] = r
            best = max(best, r - l)
        return best
            
                                

            