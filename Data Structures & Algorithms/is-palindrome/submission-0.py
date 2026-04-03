class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sol = ""

        for w in s:
            if w.isalnum():
                sol += w.lower()
        
        if sol == sol[::-1]:
            return True
        return False
        