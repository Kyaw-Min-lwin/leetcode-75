class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        # ({)}
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and (stack[len(stack) - 1] == '(' and s[i] == ')'):
                stack.pop()
            elif stack and (stack[-1] == '{' and s[i] == '}'):
                stack.pop()
            elif stack and (stack[-1] == '[' and s[i] == ']'):
                stack.pop()
            elif (s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            else:
                return False
        if stack == []:
            return True
        else:
            return False
