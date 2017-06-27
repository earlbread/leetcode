/**
 * @param {number} n
 * @return {number}
 */
var findNthDigit = function(n) {
    let len = 1;
    let number = 1;
    let count = 9;

    while (n > count * len) {
        n -= count * len;

        len += 1;
        count *= 10;
        number *= 10;
    }

    number += Math.floor((n - 1) / len);

    return parseInt(number.toString()[(n - 1) % len]);
};

let main = () => {
  console.log(findNthDigit(10));
  console.log(findNthDigit(21));
  console.log(findNthDigit(100));
  console.log(findNthDigit(1000));
}

if (require.main === module) {
  main();
}
