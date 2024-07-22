class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
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
        