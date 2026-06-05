class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chs = {}
        cht = {}

        for i in range(len(s)):
            if s[i] not in chs.keys():
                chs[s[i]] = 1
            else:
                chs[s[i]] = chs[s[i]] + 1
            
            if t[i] not in cht.keys():
                cht[t[i]] = 1
            else:
                cht[t[i]] = cht[t[i]] + 1
        
        print (chs)
        print (cht)
        if chs == cht:
            return True
        return False