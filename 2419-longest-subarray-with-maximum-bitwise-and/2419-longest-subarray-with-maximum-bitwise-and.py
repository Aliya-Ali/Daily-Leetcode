class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res , curr_size = 0, 0
        max_num = 0
        for n in nums:
            if n > max_num:
                max_num = n
                curr_size = 1
                res = 0
            elif n == max_num:
                curr_size += 1
            else:
                curr_size = 0
            
            res = max(res, curr_size)
        return res
        
        
    def longestSubarray1(self, nums: List[int]) -> int:
        max1 = max(nums)
        res , curr_size = 0, 0 
        for n in nums:
            if n == max1:
                curr_size += 1
            else:
                curr_size = 0
            res = max(curr_size, res)
        return res
                
        