/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    var amountList = [];
    var i, j;

    amountList[0] = 0;

    for (i = 0; i < amount + 1; i++) {
        for (j = 0; j < coins.length; j++) {
            if (coins[j] <= i) {
                var prev = amountList[i - coins[j]];

                if (prev !== undefined && (!amountList[i] || prev + 1 < amountList[i])) {
                    amountList[i] = prev + 1;
                }
            }
        }
    }

    return amountList[amount] !== undefined ? amountList[amount] : -1;
};

var main = function() {
  coins = [1, 2, 5];
  amount = 11;

  console.log(coinChange(coins, amount));
}

if (require.main === module) {
  main();
}
