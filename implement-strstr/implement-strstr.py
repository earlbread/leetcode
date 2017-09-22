class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0

        if not haystack:
            return -1

        if not needle:
            return 0

        i = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i] == needle[0]:
                j = 1

                while i + j < len(haystack) and j < len(needle):
                    if haystack[i+j] != needle[j]:
                        break
                    j += 1

                if j == len(needle):
                    return i

            i += 1

        return -1

s = Solution()
print(s.strStr('mississippi', 'pi'))
print(s.strStr('mississippi', 'issip'))
