class Solution:
    def isValid(self, s: str) -> bool:
        brac = {')':'(','}':'{',']':'['}
        stack = []

        for b in s:
            if b not in brac:
                stack.append(b)
            elif stack and stack[-1] == brac[b]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False




