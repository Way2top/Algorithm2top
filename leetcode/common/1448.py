from structure import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return
        count = 0
        def dfs(node: TreeNode, maxVal: int):
            if node is None:
                return
            if node.val >= maxVal:
                nonlocal count
                count += 1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, root.val)
        return count

