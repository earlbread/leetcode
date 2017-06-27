/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  var i;
  var complements = {};

  for (i = 0; i < nums.length; i++) {
    if (nums[i] in complements) {
      return [complements[nums[i]], i];
    } else {
      complements[target - nums[i]] = i;
    }
  }

  throw 'Something is wrong';
};

var main = function() {
  var nums = [2, 7, 11, 15];
  var target = 9;

  console.log(twoSum(nums, target));
};

if (require.main === module) {
  main();
}
