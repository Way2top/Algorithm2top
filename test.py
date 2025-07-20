class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        while True:
            if len(word) >= k:
                return word[k - 1]

            tmp = word[:]
            for i, ch in enumerate(tmp):
                if ch == 'z':
                    tmp[i] = 'a'
                    word.append(tmp[i])
                else:
                    tmp[i] = chr(ord(ch) + 1)
                    word.append(tmp[i])
                    
            

s = Solution()
print(s.kthCharacter(10))