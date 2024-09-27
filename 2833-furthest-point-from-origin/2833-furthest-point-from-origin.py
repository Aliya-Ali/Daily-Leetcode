class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = 0
        count_ = 0
        for i in range(len(moves)):
            if moves[i] == "L":
                count -=1
            elif moves[i] == "R":
                count +=1
            else:
                count_ +=1
        return abs(count) + count_
                
                
        