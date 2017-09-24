class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        h1 = {}
        h2 = {}

        strList = str.split(' ')

        if len(strList) != len(pattern):
            return False

        for i in range(len(strList)):
            if not h1.get(pattern[i]) and not h2.get(strList[i]):
                h1[pattern[i]] = strList[i]
                h2[strList[i]] = pattern[i]
            elif not h1.get(pattern[i]) and h2.get(strList[i]):
                return False
            elif h1.get(pattern[i]) != strList[i]:
                return False

        return True
