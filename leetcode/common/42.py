class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        pre_max = suf_max = 0
        ans = 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            # 核心逻辑
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
        