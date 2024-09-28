class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coord = []
        for i in range(len(points)):
            heapq.heappush(x_coord, points[i][0])
        res = 0
        prev = heapq.heappop(x_coord)
        while x_coord:
            curr = heapq.heappop(x_coord)
            res = max(res, curr - prev)
            prev = curr
        return res
        
        
    def maxWidthOfVerticalArea1(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        for i in range(len(points)-1):
            res = max(res,points[i+1][0] - points[i][0])
        return res
    
        