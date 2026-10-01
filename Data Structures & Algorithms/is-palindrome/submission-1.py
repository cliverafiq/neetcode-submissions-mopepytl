class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sol = ""

        for l in s:
            if l.isalnum():
                sol+=(l.lower())

        if sol == sol[::-1]:
            return True
        return False