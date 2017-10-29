class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        is_onebit = False

        i = 0

        while i < len(bits):
            if bits[i] == 1:
                is_onebit = False
                i += 1
            elif bits[i] == 0:
                is_onebit = True
            i += 1

        return is_onebit
