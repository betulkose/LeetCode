class Solution(object):
    def isValid(self, s):
        stack = []

        def eslesen(ac, kapali):
            if ac == '(' and kapali == ')':
                return True
            elif ac == '[' and kapali == ']':
                return True
            elif ac == '{' and kapali == '}':
                return True
            return False

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or not eslesen(stack.pop(), i):
                    return False

        return not stack
