class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []
        correct = {'(':')', '{':'}', '[':']'}
        
        for p in s:
            if p not in list(correct.values()):
                stack.append(p)
            
            elif stack:
                cur = stack.pop()
                if correct[cur] != p:
                    return False
            
            else:
                return False
        
        if not stack:
            return True
        return False

        