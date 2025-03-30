class validparentless:


    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' or i == ']' or i == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(' and i == ')' or stack[-1] == '[' and i == ']' or stack[-1] == '{' and i == '}':
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
