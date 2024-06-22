class Solution:
    # basket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp ={}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        # dictionary to count the number of occursion in nums
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
        
        # we make number of count an index and save the elements 
        for n, ind in mp.items():
            freq[ind].append(n)
        
        #print(freq)
        #now reversing the frequent list and saving them to our list
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                #print(n)
                res.append(n)
                if len(res) == k:
                    return res

        