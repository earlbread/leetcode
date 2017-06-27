/**
 * Definition for a binary tree node.
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    var result = [];

    if (root === null) {
        return result;
    }

    current = [root];
    children = [];

    while (current.length > 0) {
        var values = [];
        for (var i = 0; i < current.length; i++) {
            values.push(current[i].val);

            if (current[i].left) {
                children.push(current[i].left);
            }

            if (current[i].right) {
                children.push(current[i].right);
            }
        }
        result.push(values);
        current = children;
        children = [];
    }
    return result;
};

const main = () => {
  const root = new TreeNode(3);
  root.left = new TreeNode(9)
  root.right = new TreeNode(20)
  root.left.right = new TreeNode(4)
  root.right.left = new TreeNode(15)
  root.right.right = new TreeNode(7)

  console.log(levelOrder(root));
}

if (require.main === module) {
  main();
}
