from sortedcontainers import SortedList
from itertools import accumulate
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix) , len(matrix[0])
        max_sum = float('-inf')
        for left in range(n):
            temp = [0] * m
            for right in range(left, n):
                for i in range(m):
                    temp[i] += matrix[i][right]

                #kadane's algorithm to find the maximum sum of a subarray with sum less than or equal to k
                cum_sum = 0
                cum_sum_set = sorted([0])
                for t in temp:
                    cum_sum +=t
                    ind = bisect_left(cum_sum_set, cum_sum -k)
                    if ind != len(cum_sum_set):
                        max_sum = max(max_sum, cum_sum - cum_sum_set[ind])
                    bisect.insort(cum_sum_set, cum_sum)
        return max_sum

    def maxSumSubmatrix2(self, matrix: List[List[int]], k: int) -> int:
        def rangeSum1(row_M, limit):
            lst = SortedList([0])
            prefixSum  = accumulate(row_M)
            best = float('-inf')
            for s in prefixSum:
                #print(s)
                ind = lst.bisect_left(s - limit)
                if ind < len(lst):
                    x = lst[ind]
                    best = max(best, s - x)
                lst.add(s)
            return best

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += matrix[i-1][j]

        matrix = [[0 for i in range(len(matrix[0]))]] + matrix

        best = float('-inf')
        #take every combination of two rows
        for r1, r2 in combinations(range(len(matrix)), 2):
            row = [s2- s1 for s1, s2 in zip(matrix[r1], matrix[r2])]
            s = rangeSum1(row, k)
            best = max(best, s)
        return best

    def maxSumSubmatrix1(self, matrix: List[List[int]], k: int) -> int:
        R = len(matrix)
        C = len(matrix[0])
        max_sum = 0
        
        for i in range(R):
            sum_c = 0
            for j in range(C):
                sum_c += matrix[i][j]
                # print(sum_c)
            # print(sum_c)
            if max_sum + sum_c <= k:
                max_sum = max(max_sum, max_sum + sum_c)
        return max_sum
        