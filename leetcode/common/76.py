from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        target = len(counter_t)
        counter_s = Counter()
        ok_s = 0 # 记录 s 中满足 counter_t 中字符的个数，如果 ok_s = len(counter_t) 即可说明子串包含了 t
        left = 0
        ans_left = -1
        ans_right = len(s)
        for right, ch in enumerate(s):
            counter_s[ch] += 1
            # 判断 counter_s 是否包含 counter_t
            # 当字符数量首次达标时，ok_s 才加 1，达标后在遇到相同字符不应该相加
            if ch in counter_t and counter_s[ch] == counter_t[ch]:
                ok_s += 1
            while ok_s == target:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                
                # 我们现在要移出去的这个字符是在 counter_t 中的，并且数量刚好满足；那么移除之后就刚好不满足了，所以 ok_s -= 1
                if s[left] in counter_t and counter_s[s[left]] == counter_t[s[left]]:
                    ok_s -= 1
                
                counter_s[s[left]] -= 1
                left += 1
        return '' if ans_left < 0 else s[ans_left: ans_right + 1]
        