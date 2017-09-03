class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numList = list(map(int, list(str(num))))

        for i in range(len(numList)):
            maxIndex = i
            for j in range(i, len(numList)):
                if numList[maxIndex] <= numList[j]:
                    maxIndex = j
            if maxIndex != i and numList[i] < numList[maxIndex]:
                numList[i], numList[maxIndex] = numList[maxIndex], numList[i]
                break

        return int(''.join(map(str, numList)))
