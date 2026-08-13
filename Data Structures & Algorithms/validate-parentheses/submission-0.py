class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if len(stack) == 0:
                stack.append(bracket)
            else:
                match stack[-1]:
                    case "(":
                        if bracket == ")":
                            stack.pop()
                        else:
                            stack.append(bracket)
                    case "{":
                        if bracket == "}":
                            stack.pop()
                        else:
                            stack.append(bracket)
                    case "[":
                        if bracket == "]":
                            stack.pop()
                        else:
                            stack.append(bracket)
        if len(stack) == 0:
            return True
        else:
            return False
                        


