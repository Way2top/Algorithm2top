# Leetcode:658
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        n = len(arr)
        # 如果 x 在数组左边或者数组右边（包括左右边界）
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[n - k :]
        # 如果 x 在数组中间
        left = 0
        right = n - 1
        ans = []
        while left < right:
            if abs(arr[left] - x) <= abs(arr[right] - x) and k > 0:
                ans.append(arr[left])
                left += 1
                k -= 1
            elif abs(arr[left] - x) > abs(arr[right] - x) and k > 0:
                ans.append(arr[right])
                right -= 1
                k -= 1
            else:
                break
        return ans


s = Solution()
res = s.findClosestElements([-2, -1, 1, 2, 3, 4, 5], 7, 3)
print(res)
