class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_p = {')':'(',']':'[','}':'{'}

        
        
        for c in s:
            if c in close_p:
                if stack and stack[-1]==close_p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        if len(stack) ==0:
            return True 
        else:
            return False