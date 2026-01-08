class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        left, right = 0, len(plants) - 1
        ca = capacityA
        cb = capacityB
        ans = 0
        while left <= right:
            if left != right:
                if ca >= plants[left]:
                    ca -= plants[left]
                else:
                    # 题目确保了水桶的量一定大于任意一个花盆的需求
                    ans += 1
                    ca = capacityA - plants[left]
                left += 1
                    
                if cb >= plants[right]:
                    cb -= plants[right]
                else:
                    ans += 1
                    cb = capacityB - plants[right]
                right -= 1
                
            else: # left == right，二者相遇
                if ca >= cb:
                    if ca >= plants[left]: # 水够
                        ca -= plants[left]
                    else: # 水不够
                        ans += 1
                        ca = capacityA - plants[left] # 其实这一步没必要，因为已经走到最后一步了，二者已经相遇
                    left += 1
                        
                else: # ca < cb
                    if cb >= plants[left]:
                        cb -= plants[left]
                    else:
                        ans += 1
                        cb = capacityB - plants[left]
                    right -= 1
        return ans