from structure import TreeNode

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        dict = {val: idx for idx, val in enumerate(inorder)}
        # 已知 左中右 左右中
        self.currInOrder = len(postorder) - 1
        def build(inLeft: int, inRight: int) -> TreeNode:
            if inLeft > inRight:
                return None

            rootVal = postorder[self.currInOrder]
            self.currInOrder -= 1
            root = TreeNode(rootVal)

            # 找出 inorder 中 根节点的索引
            rootIdx = dict[rootVal]

            root.right = build(rootIdx + 1, inRight)
            root.left = build(inLeft, rootIdx - 1)
            return root
        return build(0, len(inorder) - 1)
