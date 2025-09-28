from structure import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while len(queue) > 0:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue[0]
                queue = queue[1:]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res