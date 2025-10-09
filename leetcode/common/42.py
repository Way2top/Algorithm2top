# class Solution:
#     def trap(self, height: list[int]) -> int:
#         # 面积怎么算？
#         # 只要存在低谷，就可以存雨水
#         # 假设低谷的左右边界高度分别为 hLeft hRight
#         # 那么有 h = min(hLeft, hRight)
#         # 然后再 （hLeft, hRight）这个开区间内遍历for i in range(left + 1, right)，res += h - height[i]

#         # 综上，可以总结出解题步骤
#         # step1：找出所有的低谷的左右边界
#         # step2：遍历这些低谷，然后 res += h - height[i]

#         # step1：对于left 和 right来说，如果中间的所有元素都小于 min(height[left], height[right])，那么就算是存在低谷
#         n = len(height)
#         valley = []
#         left = 0
#         while right < n:
#             hLeft = height[left]
#             if hLeft == 0:
#                 continue
#             for right in range(n):
#                 hRight = height[right]
#                 if hRight <= hLeft:
#                     continue
#                 else: # hRight > hLeft
#                     if hRight - hLeft - 1 > 0:
#                         valley.append([left, right])
#                     else:
#                         left = right
#                         right += 1
#                         break


# # 暴力，会超时
# class Solution:
#     def trap(self, height: list[int]) -> int:
#         n = len(height)
#         res = 0
#         for i in range(1, n - 1):
#             hLeft = max(height[:i])
#             hRight = max(height[i+1:])
#             level = min(hLeft, hRight)
#             if level > height[i]:
#                 res += level - height[i]
#         return res

# 优化方法1：动态规划——空间换时间
# 我们前面的暴力算法超时，就是因为对于每次遍历到的位置，我们都要重复的去其左侧和右侧找最大值，这个过程导致我们的复杂度到了 N 的平方
# 那么我们可以考虑提前把每个位置的左侧最大值和右侧最大值算出来
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        leftMax = [0] * n
        rightMax = [0] * n
        leftMaxVal = 0
        rightMaxVal = 0
        for i in range(n):
            leftMaxVal = max(leftMaxVal, height[i]) 
            leftMax[i] = leftMaxVal
        for i in range(n - 1, -1, -1):
            rightMaxVal = max(rightMaxVal, height[i])
            rightMax[i] = rightMaxVal
        # 此时我们就可以通过 leftMax 和 rightMax 来查询到第 i 个元素的左侧最大值和右侧最大值了
        for i in range(1, n - 1):
            level = min(leftMax[i], rightMax[i])
            if level > height[i]:
                res += level - height[i]
        return res

# 优化方法2：双指针
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        leftMax = rightMax = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                # 那么说明 level 一定等于 leftMax
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
                right -= 1
        return res