class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = defaultdict(int)
        arr_set = set(arr2)
        end = []
        for i in arr1:
            if i not in arr_set:
                end.append(i)
            mp[i] += 1
        end.sort()
        res =[]
        for n in arr2:
            for i in range(mp[n]):
                res.append(n)
                
        return res +end
        
        
    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    num.append(arr2[i])
            arr1.remove(arr2[i])
        print(arr1)
        arr1.sort()
        for i in arr1:
            num.append(i)
        return num
            
        