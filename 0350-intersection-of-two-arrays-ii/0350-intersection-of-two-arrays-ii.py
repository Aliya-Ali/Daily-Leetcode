class Solution:
    def intersect(self, nums1: List[int] ,  nums2:List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1) , sorted(nums2)
        res = []
        i, j= 0,0
        while i< len(nums1) and j <len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res

    def intersect2(self, nums1: List[int] , nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        res =[]
        for n in nums2:
            if c[n] >0:
                res.append(n)
                c[n] -=1
        return res

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
                nums2.remove(n)
        return res