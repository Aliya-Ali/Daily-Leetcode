class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        r = 10**9
        while l<= r:
            mid = (l + r)//2
            total_dis_per_hour = 0
            for n in range(len(dist) -1):
                total_dis_per_hour += math.ceil(dist[n]/mid)
            total_dis_per_hour += dist[-1]/mid
            
            #print(total_dis_per_hour)
            if total_dis_per_hour <= hour:
                r = mid - 1
            else:
                l = mid + 1
        
        if l > 10**9:
            return -1
        else:
            return l
        
                