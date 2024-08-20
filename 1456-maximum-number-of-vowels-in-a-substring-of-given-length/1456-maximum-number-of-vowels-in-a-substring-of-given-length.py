class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set_array = set(['a','e','i','o', 'u'])
        count = 0
        res =0
        for i, e in enumerate(s):
            if i>= k  and s[i-k] in set_array:
                count -=1
            if e in set_array:
                count +=1
                res = max(res, count)
        return res
    
    def maxVowels1(self, s: str, k: int) -> int:
        l = 0
        r = 0
        set_array = set()
        res = 0 
        for r in range(len(s)):
            if (r-l)> k:
                set_array.remove(s[l])
                l += 1
            if s[r] in "aeiou":
                set_array.add(s[r])
                res = max(res, r - l + 1)
        return res
                
        