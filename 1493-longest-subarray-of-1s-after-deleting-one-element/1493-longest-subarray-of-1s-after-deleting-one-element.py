class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count = 0
        max_1 = 0
        zero = 0
        while right < len(nums):
            if nums[right] == 0:
                zero +=1
            if zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left +=1
            count = right - left
            max_1 = max(count, max_1)
            right +=1
        return max_1
        