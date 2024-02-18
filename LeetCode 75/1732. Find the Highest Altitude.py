class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        current = 0
        for g in gain:
            current += g
            if(current > max):
                max = current
        return max
