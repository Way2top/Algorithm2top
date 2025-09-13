class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        t = [''] * len(s)
        dict = {}
        for idx, ch in enumerate(s):
            if ch.lower() not in vowels:
                t[idx] = ch
                continue
            else:
                dict[idx] = dict.get(idx, ch) 
        keys = list(dict.keys())
        values = sorted(list(dict.values()))
        for i in range(len(keys)):
            t[keys[i]] = values[i]
                
        return ''.join(t)

s = Solution()
res = s.sortVowels("lEetcOde")
print(res)