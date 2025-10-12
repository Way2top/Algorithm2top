from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ns = len(s)
        np = len(p)
        if np > ns:
            return []
        target = Counter(p)
        res = []

        left = 0
        right = np - 1
        window = Counter(s[:np]) # 初始化窗口

        while True:
            if window == target:
                res.append(left)
            window[s[left]] -= 1
            left += 1

            right += 1
            if right >= ns:
                break
            window[s[right]] += 1
        return res
        