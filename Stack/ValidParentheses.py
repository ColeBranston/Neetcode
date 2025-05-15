class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # stack for proper opening and closing brackets
        closeToOpen = {  # hashmap for proper bracket categorization
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in closeToOpen:  # checks if the bracket type is in the categorizations hashmap
                # checks if the stack isn't empty and if the top most element on the stack is the same as the current categorization assignemtn fo the current bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # removes the top most element of the stack

                else:  # if either the stack is empty or the top most element doesn't match the matching closing bracket for the current bracket in the string
                    return False

            else:  # if the current bracket isn't in the stack then its therefore an opening bracket, meaning that it will be added to the stack
                stack.append(c)

        # returns true almost everytime but before safety checks if the stack is empty to ensure its a correct sequence
        return True if not stack else False
