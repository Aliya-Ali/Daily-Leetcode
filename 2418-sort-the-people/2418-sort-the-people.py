class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = []
        for i in range(len(heights)):
            a.append([ heights[i], names[i]])
        
        a.sort(reverse = True)
        
        b = []
        for i in range(len(a)):
            b.append(a[i][1])
        return b