# Leetcode:2094
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        n = len(digits)
        res = set()
        for num in range(100, 1000):
            # num must be a even number
            if num % 2 != 0:
                continue
            
            num_digits = [num // 100, (num // 10) % 10, num % 10]
            digits_copy = digits[:]
            valid = True
            
            for d in num_digits:
                if d in digits_copy:
                    digits_copy.remove(d)
                else:
                    valid = False
                    break
            
            if valid:
                res.add(num)
        return sorted(res)