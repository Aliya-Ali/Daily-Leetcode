class Solution:
    def isPerfectSquare(self, num:int) -> bool:
        l = 1
        r = num
        mid = (l + num)//2;
        while mid **2 > num:
            mid = (l+ mid)//2;
        
        while mid ** 2 <= num:
            if mid **2 == num:
                return True
            mid +=1
        return False
        
        
            
    # it is very slow
    def isPerfectSquare1(self, num: int) -> bool:
        n = 1
        while n**2 <= num:
            if n**2 == num:
                return True
            n +=1
        return False
            
        