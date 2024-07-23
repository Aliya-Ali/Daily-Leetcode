class Solution:
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                if i- mp[nums[i]] <= k:
                    return True
                mp[nums[i]] = i
                
            else:
                mp[nums[i]] = i
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int)-> bool:
        window = set()
        for i in range(len(nums)):
            if nums[i] in window: return True
            
            window.add(nums[i])
            
            if len(window) > k:
                window.remove(nums[i-k])
        return False
        