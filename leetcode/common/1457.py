from structure import TreeNode

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        digit = [0] * 10
        if root is None:
            return 0
        count = 0
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            digit[node.val] ^= 1
            if node.left is None and node.right is None:
                res = 1 if sum(digit) <= 1 else 0
            else:
                res = dfs(node.left) + dfs(node.right)
            digit[node.val] ^= 1
            return res
        return dfs(root)