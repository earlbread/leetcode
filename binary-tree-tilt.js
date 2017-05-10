/**
 * Definition for a binary tree node.
 */

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var findSumAndTilt = function(root) {
    if (root === null) {
        return [0, 0];
    }

    var [left_sum, left_tilt] = findSumAndTilt(root.left);
    var [right_sum, right_tilt] = findSumAndTilt(root.right);

    var sum = left_sum + right_sum + root.val;
    var tilt = left_tilt + right_tilt + Math.abs(left_sum - right_sum);

    return [sum, tilt];
};

var findTilt = function(root) {
    return findSumAndTilt(root)[1];
};

var main = function() {
    var root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    root.left.left = new TreeNode(4)
    root.left.right = new TreeNode(5)
    root.right.left = new TreeNode(6)
    root.right.right = new TreeNode(7)

    console.log(findSumAndTilt(root)[1]);
}

if (require.main === module) {
    main();
}
