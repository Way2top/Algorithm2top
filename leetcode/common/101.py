from structure import TreeNode

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(p: TreeNode, q: TreeNode) -> bool:
            if p is None or q is None:
                return p is q


        dfs(root.left, root.right)