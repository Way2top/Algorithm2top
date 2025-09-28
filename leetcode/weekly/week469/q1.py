class Solution:
    def decimalRepresentation(self, n: int) -> list[int]:
        def getDigit(n : int) -> list[int]:
            res = []
            while n > 0:
                res.append(n % 10)
                n //= 10
            res.reverse()
            return res
        digit = getDigit(n)
        cloth = len(digit) - 1
        res = []
        for i, n in enumerate(digit):
            if n == 0:
                cloth -= 1
                continue
            res.append(n * (10 ** cloth))
            cloth -= 1
        return res