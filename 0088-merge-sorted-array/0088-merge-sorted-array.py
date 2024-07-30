class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n =int) -> None:
        last = m + n -1
        while m>0 and n> 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -=1
            else:
                nums1[last] = nums2[n-1]
                n -=1
            last -=1 
        while n>0:
            nums1[last] = nums2[n-1]
            n , last = n-1 , last -1
            
                
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i =0 
        j = 0
        if m == 0 and n ==1 :  nums1[0] = nums2[0]
             
        while i<m and j<n:
            if nums1[i] > nums2[j]:
                temp = nums1[i]
                nums1[i] = nums2[j]
                nums2[j] = temp
                j+=1

            i +=1
        print
        j = 0 
        while j<len(nums2):
            nums1[i] = nums2[j]
            i+=1
            j+=1
        print(nums1)
            
        
        