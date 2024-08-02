class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left_arr = arr[L: M+1]
            right_arr = arr[M+1 : R+1]
            i = L
            j , k= 0, 0
            while (j <len(left_arr) and k <len(right_arr)):
                if left_arr[j]<= right_arr[k]:
                    arr[i] = left_arr[j]
                    j+=1
                else:
                    arr[i] = right_arr[k]
                    k+=1
                i+=1
            while (j < len(left_arr)):
                arr[i] = left_arr[j]
                i +=1
                j +=1
            while k <len(right_arr):
                arr[i] = right_arr[k]
                i+=1
                k+=1
        
        
        
        def mergesort(arr, l, r):
            if l == r:
                return arr
            
            m = (l + r)//2
            mergesort(arr, l, m)
            mergesort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        
        return mergesort(nums, 0, len(nums)-1)
        
        
        
    #insertion sort: the partition the nums into two part and sort the one
    def sortArray2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, len(nums)):
            key = nums[i]
            j = i-1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key
        return nums
        
        
        
    def sortArray1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n-1):
            min_ind = i
            for j in range(i+1, n):
                if nums[min_ind] > nums[j]:
                    min_ind = j
            temp = nums[i]
            nums[i] = nums[min_ind]
            nums[min_ind] = temp
        return nums