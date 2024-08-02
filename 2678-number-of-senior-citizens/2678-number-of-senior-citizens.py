class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for str1 in details:
            #print(str1[11:13])
            if int(str1[11:13]) > 60:
                count+=1
        return count
        