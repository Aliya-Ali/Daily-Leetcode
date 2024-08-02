class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        j = 0
        nums1 = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        for i in range(len(even)):
            nums1.append(even[i])
            j+=1
            nums1.append(odd[i])
        return nums1