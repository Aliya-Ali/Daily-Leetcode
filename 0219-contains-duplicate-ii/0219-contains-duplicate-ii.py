class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        set_Array = set()
        for right in range(len(nums)):
            if (right - left) > k:
                set_Array.remove(nums[left])
                left+=1
            if nums[right] in set_Array:
                return True
            set_Array.add(nums[right])
        return False
    
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        left = 0
        for right in range(len(nums)): 
            if right - left >k:
                left += 1
            if nums[right] == nums[left] and right != left:
                return True
            print(left)
            print(right)
        return False
            
                
        