class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        oper = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            print(stack)
            if i in oper:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if i == oper[0]:
                    stack.append(val1+val2)
                elif i == oper[1]:
                    stack.append(val2-val1)
                elif i == oper[2]:
                    val = val1*val2
                    stack.append(val)
                elif i == oper[3]:
                    if val1 == 0 or val2 == 0:
                        stack.append(0)
                    else:
                        stack.append(val2/val1)
            else:
                stack.append(i)
        return int(stack.pop())
            

                
                    
