class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        n = len(chars)

        i = 0
        p = 0

        while i < n:
            prev = i
            i += 1

            while i < n and chars[i] == chars[prev]:
                i += 1

            chars[p] = chars[prev]
            p += 1

            if i - prev > 1:
                for c in str(i - prev):
                    chars[p] = c
                    p += 1

        return p

