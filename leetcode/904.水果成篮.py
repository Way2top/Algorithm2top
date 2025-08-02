# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#


# @lc code=start
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # equivalent to finding the longest subarray that contains at most 2 different elements.
        types = {}
        res = temp = 0
        left = 0
        for right, fruit in enumerate(fruits):
            types[fruit] = types.get(fruit, 0) + 1
            temp += 1
            while len(types.keys()) > 2:
                types[fruits[left]] -= 1
                temp -= 1
                if types[fruits[left]] == 0:
                    del types[fruits[left]]
                left += 1
            res = max(res, temp)
        return res


# @lc code=end
