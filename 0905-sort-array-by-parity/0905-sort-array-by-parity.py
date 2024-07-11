class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = []
        arr1 = []
        for i in range(len(nums)):
            if nums[i] %2 == 0:
                arr.append(nums[i])
            else:
                arr1.append(nums[i])
        for i in arr1:
            arr.append(i)
        return arr
        
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        while l< r:
            if nums[l] %2 != 0 and nums[r] % 2==0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            elif nums[l] % 2 == 0:
                l+=1
            elif nums[r] %2 != 0:
                r-=1
        return nums
            
        