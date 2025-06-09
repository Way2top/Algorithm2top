class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1]]
        
        ans = [[0 for _ in range(n)] for _ in range(n)]
        start_x = 0  # 每一轮转圈的起始x坐标
        start_y = 0  # 每一轮转圈的起始y坐标
        length = n   # 每一轮循环的边界
        cur = 0
        
        # 修正：循环次数应为 (n+1)//2，确保奇数n时中心元素被填充
        for _ in range((n + 1) // 2):
            # 向右填充
            for j in range(start_y, length):
                cur += 1
                ans[start_x][j] = cur
            
            # 向下填充
            for i in range(start_x + 1, length):
                cur += 1
                ans[i][j] = cur  # j此时指向最右列
            
            # 向左填充（要求至少有两行）
            if start_x != length - 1:
                for j in range(length - 2, start_y - 1, -1):
                    cur += 1
                    ans[i][j] = cur  # i此时指向最下行
            
            # 向上填充（要求至少有两列）
            if start_y != length - 1:
                for i in range(length - 2, start_x, -1):
                    cur += 1
                    ans[i][j] = cur  # j此时指向最左列
            
            # 更新起始点和边界
            start_x += 1
            start_y += 1
            length -= 1
        
        # 修正：当n为奇数时，正确填充中心元素
        if n % 2 == 1:
            ans[n//2][n//2] = n * n
            
        return ans