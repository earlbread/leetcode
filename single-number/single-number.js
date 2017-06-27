/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  var i;
  var result = 0;
  for (i = 0; i < nums.length; i++) {
    result ^= nums[i];
  }
  return result;
};

var main = function() {
  var nums = [1, 1, 3, 2, 2];

  console.log(singleNumber(nums));
}

if (require.main === module) {
  main();
}
