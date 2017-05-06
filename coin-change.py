class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        amount_list = []
        amount_list = [-1] * (amount + 1)
        amount_list[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    prev = amount_list[i - c]

                    if (prev != -1 and
                       (amount_list[i] == -1 or prev + 1 < amount_list[i])):
                        amount_list[i] = prev + 1

        return amount_list[amount]



if __name__ == '__main__':
    s = Solution()

    coins_list = [
            [1, 2, 5],
            [2],
            [186,419,83,408],
    ]

    amount_list = [
            11,
            3,
            6249,
    ]

    for i in range(len(coins_list)):
        print(s.coinChange(coins_list[i], amount_list[i]))
