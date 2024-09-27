class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        move_point = 0
        count_ = 0
        for i in range(len(moves)):
            if moves[i] == 'L':
                move_point -=1
            elif moves[i] == "R" :
                move_point += 1
            else:
                count_ +=1
                
                
        return abs(move_point)+ count_ 
                
        