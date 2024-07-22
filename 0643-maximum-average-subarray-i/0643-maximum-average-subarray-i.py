class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k])
        for i in range(len(nums) - k):
            curr_sum = curr_sum - nums[i] + nums[i+k]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum/k
                
        
    def findMaxAverage1(self, nums: List[int], k: int) -> float:
        sum_arr_k = 0
        for i in range(k):
            sum_arr_k += nums[i]
        max_avg = (sum_arr_k)/k
        for i in range(k,len(nums)):
            sum_arr_k -= nums[i-k]
            sum_arr_k += nums[i]
            curr_avg = sum_arr_k /k
            if curr_avg > max_avg:
                max_avg = curr_avg
        return max_avg
        