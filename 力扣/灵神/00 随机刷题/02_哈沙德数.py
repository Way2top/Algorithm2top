class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit = [] # 倒序存储每一位
        xx = x
        while x != 0:
            digit.append(x % 10)
            x = x // 10
        if xx % sum(digit) == 0:
            return sum(digit)
        else:
            return -1
s = Solution()
print(s.sumOfTheDigitsOfHarshadNumber(23))