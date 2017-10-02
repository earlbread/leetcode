class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        def countWord(s, start):
            count = 0
            for i in range(start, len(s)):
                if s[i] == ' ':
                    return count, i + 1
                count += 1
            return count, i + 1

        count = 0
        start = 0

        if not s:
            return count

        while start < len(s):
            if s[start] != ' ':
                count, start = countWord(s, start)
            else:
                start += 1

        return count

