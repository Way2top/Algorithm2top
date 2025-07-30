import bisect


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        m = len(queries)
        ans = [0] * m

        # nums 的顺序没有任何影响，排序后计算前缀和
        nums.sort()
        prefix = [0] * n
        for i in range(n):
            if i == 0:
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i - 1] + nums[i]
            # [1, 2, 4, 5] -- nums
            # [1, 3, 7, 12] -- prefix

        for i in range(m):
            temp = bisect.bisect(prefix, queries[i])
            ans[i] = temp
        return ans


s = Solution()
res = s.answerQueries([4, 5, 2, 1], [3, 10, 21])
print(res)
