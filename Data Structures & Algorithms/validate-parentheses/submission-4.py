class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        correct = {'(':')', '{':'}', '[':']'}
        for p in s:
            if p not in list(correct.values()):
                stack.append(p)
                print("1")
            elif stack:
                print("2")
                cur = stack.pop()
                if correct[cur] != p:
                    return False
            else:
                print("3")
                return False
        
        if not stack:
            return True
        return False

        