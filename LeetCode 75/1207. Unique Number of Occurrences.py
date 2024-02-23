class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}

        for i in arr:
            current = occ.get(i, 0)  # Default value is 0 if key doesn't exist
            occ[i] = current + 1

        unique = set()

        for key in occ.values():
            if (key in unique):
                return False
            unique.add(key)
        return True