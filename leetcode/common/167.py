# 哈希表
# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         dic = {}
#         for i, n in enumerate(numbers):
#             if target - n in dic:
#                 return [dic[target - n] + 1, i + 1]
#             dic[n] = i

# 双指针
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            ans = numbers[left] + numbers[right]
            if ans == target:
                return [left, right]
            elif ans > target:
                right -= 1
            else:
                left += 1
        