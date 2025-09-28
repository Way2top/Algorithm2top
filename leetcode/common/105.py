from codecs import BOM_UTF16_LE

from structure import TreeNode

# class Solution:
#     def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
#         if not preorder or not inorder:
#             return None
#         root = TreeNode(preorder[0])
#         idx = inorder.index(root.val)
#         leftInorder = inorder[:idx]
#         rightInorder = inorder[idx+1:]
#         leftPreorder = preorder[1:idx + 1]
#         rightPreorder = preorder[idx + 1:]
#         root.left = self.buildTree(leftPreorder, leftInorder)
#         root.right = self.buildTree(rightPreorder, rightInorder)
#         return root

class Solution:
    def __init__(self):
        self.currInOrder = 0

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # 构建哈希表，方便稍后查询根节点索引的速度更快（O(1)）
        dict = {val : idx for idx, val in enumerate(inorder)}
        def build(inLeft: int, inRight: int) -> TreeNode:
            if inLeft > inRight:
                return None

            # 取出当前子树的根节点
            inOrderVal = preorder[self.currInOrder]
            self.currInOrder += 1

            root = TreeNode(inOrderVal)
            rootIdx = dict[inOrderVal] # 根据前面构建的哈希表找出根节点的索引

            root.right = build(rootIdx + 1, inRight)
            root.left = build(inLeft, rootIdx - 1)
            return root
        return build(0, len(preorder) - 1)

