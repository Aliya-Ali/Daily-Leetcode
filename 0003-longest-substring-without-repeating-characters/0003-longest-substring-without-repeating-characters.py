class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        max_length = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1
            mp[s[r]] = r
            
            max_length  = max(max_length, r-l +1)
        return max_length
        
        
        
        
        
    def lengthOfLongestSubstring1(self, s: str) -> int:
        l = 0
        non_repeating_set = set()
        max_length = 0
        for r in range(len(s)):
            max_length = max(max_length, r-l)
            if s[r] in non_repeating_set:
                l += 1
            non_repeating_set.add(s[r])  
        return max_length
        