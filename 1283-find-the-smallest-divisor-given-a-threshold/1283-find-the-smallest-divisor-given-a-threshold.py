class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        
        while l<=r:
            mid = (l+r) //2
            total_sum = 0 
            for n in nums:
                total_sum += math.ceil(n/mid)
            if total_sum > threshold:
                l = mid + 1
            else:
                r = mid -1
        return l
                
                
        