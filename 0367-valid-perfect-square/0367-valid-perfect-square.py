class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while n**2 <= num:
            if n**2 == num:
                return True
            n +=1
        return False
            
        