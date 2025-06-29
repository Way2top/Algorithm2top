# Leetcode:977
# O(NlogN)
# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         ans = []
#         for n in nums:
#             ans.append(n**2)
#         return sorted(ans)
# s = Solution()
# res = s.sortedSquares([-4, -1, 0, 3, 5])
# print(res)

# O(N)   双指针
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        right = len(nums) - 1
        if left == right:
            return [nums[0]**2]
        
        ans = [0] * len(nums)
        index = len(nums) - 1
        while left <= right:
            # 比较下标为 left 与 right 的值的大小
            l_val = nums[left] ** 2
            r_val = nums[right] ** 2
            if l_val <= r_val:
                ans[index] = r_val
                index -= 1
                right -= 1
            else:
                ans[index] = l_val
                index -= 1
                left += 1
            
        return ans