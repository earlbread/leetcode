class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True

        upper = word[1].isupper()

        for i in range(2, len(word)):
            if word[i].isupper() != upper:
                return False

        if not word[0].isupper() and upper:
            return False

        return True
