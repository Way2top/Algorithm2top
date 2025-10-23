from structure import TreeNode
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            
            l_depth = dfs(node.left)
            r_depth = dfs(node.right)

            # 更新答案
            nonlocal ans
            ans = max(ans, l_depth + r_depth)

            return 1 + max(l_depth, r_depth)
        dfs(root)
        return ans