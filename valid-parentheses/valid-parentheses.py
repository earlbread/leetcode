class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_parentheses = ['(', '{', '[']
        pair = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c  in open_parentheses:
                stack.append(c)
            else:
                if not stack:
                    return False
                if pair[c] != stack.pop():
                    return False

        if stack:
            return False

        return True
