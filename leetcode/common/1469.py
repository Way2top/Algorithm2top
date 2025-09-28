from structure import TreeNode
from typing import Optional

class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        res = []
        # 如果一个节点，存在左右孩子，且只存在一个孩子，那么该结点为独生节点
        def traversal(node: TreeNode):
            if node is None:
                return
            nonlocal res
            if node.left and node.right is None:
                res.append(node.left.val)
            if node.left is None and node.right:
                res.append(node.right.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return res
