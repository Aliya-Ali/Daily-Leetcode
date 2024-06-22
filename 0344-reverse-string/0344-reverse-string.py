class Solution:
    # extra memory is needed if we use the stack and recursion 
    def reverseString(self, s: List[str]) -> None:
        def recurse(l, r):
            if l < r:
                s[l], s[r] = s[r] , s[l] 
                recurse(l+1, r -1)
        recurse(0, len(s)-1)
        
    def reverseString2(self, s: List[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i+=1
            
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l <r:
            s[l], s[r] = s[r], s[l]
            l +=1
            r -=1
        
        