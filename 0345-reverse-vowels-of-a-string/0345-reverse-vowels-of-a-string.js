class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [i for i in s]
        vowel = []
        for i in s:
            if i in "aeiouAEIOU":
                vowel.append(i)
        
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                s[i] = vowel.pop()
        
        s = "".join(s)
        return s
                
        