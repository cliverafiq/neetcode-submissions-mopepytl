class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1
        
        for x in t:
            if x not in count or count[x] == 0:
                return False
            count[x] -= 1

        return True
        