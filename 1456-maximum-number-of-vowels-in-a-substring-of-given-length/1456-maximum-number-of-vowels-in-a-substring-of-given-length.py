class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        max_count = count = 0
        
        for r in range(len(s)):
            count += 1 if s[r] in "aeiou" else 0
            if r - l + 1 > k:
                count -= 1 if s[l] in "aeiou" else 0
                l +=1
            max_count = max(max_count, count)
        return max_count
        
    def maxVowels1(self, s: str, k: int) -> int:
        count = 0
        for i in range(k):
            if s[i] in "aeiou":
                count +=1
        max_count = count
        
        for i in range(len(s) -k):
            if s[i] in "aeiou":
                count -=1
            if s[i+k] in "aeiou":
                count += 1
            
            if count > max_count:
                max_count = count
        return max_count
            