#
# @lc app=leetcode.cn id=2024 lang=python3
#
# [2024] 考试的最大困扰度
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 等价于找出一个最长子数组，这个子数组应该包含 k 个 true 或者 k 个false
        dic = {'T': 0, 'F': 0}
        res = 0
        left = 0
        for right, ans in enumerate(answerKey):
            dic[ans] = dic.get(ans, 0) + 1
            while dic['T'] > k and dic['F'] > k:
                dic[answerKey[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

# @lc code=end

