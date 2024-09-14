class Solution:
    
    def longestSubarray(self, nums: List[int]) -> int:
        max1 = max(nums)
        res , curr_size = 0, 0 
        for n in nums:
            if n == max1:
                curr_size += 1
            else:
                curr_size = 0
            res = max(curr_size, res)
        return res
                
        