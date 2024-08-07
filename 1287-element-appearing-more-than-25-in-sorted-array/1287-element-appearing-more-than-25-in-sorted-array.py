class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) ==1: return arr[0]
        freq = math.floor(len(arr) *(1/4)) 
        for i in range(len(arr) - freq):
            if arr[i] == arr[i+freq]:
                return arr[i]
        
        
        
    def findSpecialInteger1(self, arr: List[int]) -> int:
        freq = math.floor(len(arr) * (1/4))
        mp = {}
        for i in arr:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        for i in mp:
            if mp[i] > freq:
                return i
            
        