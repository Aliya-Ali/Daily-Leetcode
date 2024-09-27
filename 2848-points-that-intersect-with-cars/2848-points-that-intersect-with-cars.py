class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        seen = set()
        for s, e in nums:
            for x in range(s,e+1):
                seen.add(x)
        return len(seen)
        