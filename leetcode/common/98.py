from structure import TreeNode
from typing import Optional
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: TreeNode|None):
            if node is None:
                return True, math.inf, -math.inf
            
            l_isBST, l_minVal, l_maxVal = dfs(node.left)
            r_isBST, r_minVal, r_maxVal = dfs(node.right)

            return (l_isBST and r_isBST) and l_maxVal < node.val < r_minVal, min(node.val, l_minVal, r_minVal), max(node.val, l_maxVal, r_maxVal)
        ans, _, _ = dfs(root)
        return ans