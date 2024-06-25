class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        res = []
        for n in nums1:
            if n in mp and n in nums2:
                mp[n] +=1
            else:
                mp[n] =1
        for n in nums2:
            if n in mp and n in nums1:
                mp[n]+=1
            else:
                mp[n] = 1
        for n in mp:
            if mp[n] >1:
                res.append(n)
        return res
            
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            if n in nums2 and n not in res:
                print(n)
                res.append(n)
    
        return res
        