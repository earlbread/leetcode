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
var maxDepth = function(root) {
    if (root === null) {
        return 0;
    }

    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};

let main = () => {
  let root = new TreeNode(1);
  root.right = new TreeNode(2);

  console.log(maxDepth(root));
}

if (require.main === module) {
  main();
}
