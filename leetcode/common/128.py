class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        st = set(nums)
        res = 0
        m = len(st)
        for n in st:
            if n - 1 in st:
                continue
            temp = 1
            y = n + 1
            while y in st:
                temp += 1
                y += 1
            res = max(res, temp)
            if res * 2 >= m:
                break
        return res

s = Solution()
ans = s.longestConsecutive([100,4,200,1,3,2])
print(ans)