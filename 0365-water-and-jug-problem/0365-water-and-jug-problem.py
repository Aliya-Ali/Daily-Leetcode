class Solution:
    #breath first search
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        q = deque([0])
        seen= set()
        quantity = [x, y, -x, -y]
        while q:
            curr = q.popleft()
            for i in quantity:
                total = curr + i
                if total == target:
                    return True
                if total not in seen and 0<= total <= x + y:
                    q.append(total)
                    seen.add(total)
        return False
    
    # depth first search
    def canMeasureWater1(self, x: int, y: int, target: int) -> bool:
        seen = set()
        def dfs(total):
            if total == target:
                return True
            if total in seen or total < 0 or total > x + y:
                return False
            seen.add(total)
            
            return dfs(total + x) or dfs(total + y) or dfs(total - x) or dfs(total -y)
        return dfs(0)