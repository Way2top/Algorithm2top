class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        p = list(password)
        left = p[target:]
        right = p[:target]
        left.extend(right)
        return "".join(left)



class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        return "".join(list(password)[target:] + list(password)[:target])