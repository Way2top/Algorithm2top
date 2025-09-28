from structure import TreeNode

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        # 等价于求出所有从根节点到叶子结点的路径
        def dfs(node: TreeNode, x):
            if node is None:
                return
            x = x * 10 + node.val
            if node.left is None and node.right is None:
                nonlocal res
                res += x
                return
            dfs(node.left, x)
            dfs(node.right, x)
        dfs(root, 0)
        return res


