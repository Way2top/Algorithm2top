# Leetcode:3024
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        x = nums[0]
        y = nums[1]
        z = nums[2]

        if x == y and y == z:
            return 'equilateral'

        if (x == y or y == z or x == z) and self.is_triangle(x, y, z):
            return 'isosceles'

        if self.is_triangle(x, y, z):
            return 'scalene'
        return 'none'

    def is_triangle(self, x, y, z):
        if (x + y) > z and (x + z) > y and (y + z) > x:
            return True
        return False

s = Solution()
res = s.is_triangle
