class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        min_color = k
        white = 0
        
        while right < len(blocks):
            if blocks[right] == "W":
                white += 1
            
            while right - left + 1 > k:
                if blocks[left] == "W":
                    white -=1
                left +=1
            
            if right - left + 1 == k:
                min_color = min(min_color, white)
            right +=1
            
        return min_color
        