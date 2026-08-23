class Solution:
    def isValid(self, s: str) -> bool:
        if s == "" or len(s)%2!=0: return False

        brac = {'[':']', '{':'}', '(':')'}
        stack = []

        for i in s:
            if i in brac.keys():
                stack.append(i)
            else:
                if not stack or i != brac[stack.pop()]:
                    return False
        
        if not stack: return True
        return False

        