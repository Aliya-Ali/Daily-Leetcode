class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]* nums[-2] * nums[-3] , nums[0] * nums[1] * nums[-1])
        
        
    def maximumProduct2(self, nums: List[int]) -> int:
        max1 =  float("-inf")
        max2 = float("-inf")
        max3 = float("-inf")
        
        min1 = float("inf")
        min2 = float("inf")
        
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
            
        prod = max(max1 * max2 * max3, min1 * min2 * max1)
        return prod
    
    def maximumProduct1(self, nums: List[int]) -> int:
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        i = 0
        prod = float("-inf")
        while i <len(nums):
            if nums[i] > first:
                first = abs(nums[i])
                i +=1
            if i < len(nums) and abs(nums[i]) > second:
                second = abs(nums[i])
                i += 1
            if i < len(nums) and abs(nums[i]) > third:
                third = abs(nums[i])
                i += 1
            prod_curr = first * second * third
            prod = max(prod_curr, prod)
        return prod