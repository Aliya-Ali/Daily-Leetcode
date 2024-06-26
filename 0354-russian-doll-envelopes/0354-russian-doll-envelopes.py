class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda e: (e[0], -e[1]))
        #smallest last element
        INF = 10**20
        
        best = [-INF]
        for w, h in envelopes:
            index = bisect.bisect_left(best, h)
            
            if index >= len(best):
                best.append(h)
            else:
                best[index] = h
        return len(best)-1
                
    # time limit exceeded
    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        env = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        #print(env)
        dp = []
        
        for w, h in env:
            i = 0
            N = len(dp)
            while i< N:
                if h <= dp[i]: break
                #print(i)
                i +=1
            if i == N:
                dp.append(h)
                #print(dp)
            else:
                dp[i] = h
        #print(dp)
        return len(dp)
                