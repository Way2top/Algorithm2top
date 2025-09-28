from structure import TreeNode

class Solution:
    def numColor(self, root: TreeNode) -> int:
        if root is None:
            return 0
        dict = {}
        def inOrder(node: TreeNode):
            if node is None:
                return
            inOrder(node.left)
            inOrder(node.right)
            dict[node.val] = dict.get(node.val, 0) + 1
        inOrder(root)
        return len(dict)