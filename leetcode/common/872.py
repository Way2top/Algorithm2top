from structure import TreeNode
from typing import Optional

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inOrder(node: TreeNode) -> list[int]:
            if node is None:
                return []
            ans = []
            leftList = inOrder(node.left)
            rightList = inOrder(node.right)
            ans.extend(leftList)
            ans.extend(rightList)
            if node.left is None and node.right is None:
                ans.append(node.val)
            return ans
        res1 = inOrder(root1)
        res2 = inOrder(root2)
        return res1 == res2