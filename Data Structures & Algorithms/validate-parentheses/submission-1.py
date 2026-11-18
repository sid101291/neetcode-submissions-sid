class Solution:
    def isValid(self, s: str) -> bool:

        bracket_pairs = {
            "[":"]",
            "(":")",
            "{":"}"
        }

        stack = []

        for ch in s:

            if ch in "({[":
                stack.append(ch)
            else:

                if not stack:
                    return False 


                if bracket_pairs[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True 
        else:
            return False


        