class Solution(object):
    def isValid(self, s):
        stack = [None] * len(s)  
        index = -1  

        def eslesen(ac, kapali):
            return (ac == '(' and kapali == ')') or \
                   (ac == '[' and kapali == ']') or \
                   (ac == '{' and kapali == '}')

        for char in s:
            if char in "([{":
                index += 1
                stack[index] = char 
            else:
                if index == -1 or not eslesen(stack[index], char):
                    return False
                index -= 1  

        return index == -1
