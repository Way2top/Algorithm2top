# Fuck You!

class Solution:
    def hasSymbol(self, s: str) -> tuple[bool, str]:
        # 判断函数是否存在 + 或者 -，如果存在大于 1 个返回 False
        count = s.count('+') + s.count('-')
        ok = True
        if count > 1:
            ok = False
        # + 或者 - 只能出现在第一位（如果有）
        if '+' in s:
            if s.index('+') != 0:
                ok = False
            else:
                s = s[1:]
        if '-' in s:
            if s.index('-') != 0:
                ok = False
            else:
                s = s[1:]
        return ok, s

    def isDecimal(self, s: str) -> bool:
        ok, s = self.hasSymbol(s)
        left, right = s.split('.')
        # TODO:

    def isInteger(self, s: str) -> bool:
        ok, s = self.hasSymbol(s)
        # 此时的 s 是删去符号的



    def validNumber(self, s: str) -> bool:
        # Step1: 去掉首尾空格
        s = s.strip()

        # Step2: 分割 'e' 或者 'E'
        if 'e' in s:
            num, exp = s.split('e')
        elif 'E' in s:
            num, exp = s.split('E')
        else:
            num = s
            exp = 0

        # Step3: 判断 num 是否为小数或者整数
        isNum = False
        if '.' in num:
            isNum = self.isDecimal(num)
        else:
            isNum = self.isInteger(num)

        # Step4: 判断 exp 是否为整数
        isExp = self.isInteger(num)

        return isNum and isExp