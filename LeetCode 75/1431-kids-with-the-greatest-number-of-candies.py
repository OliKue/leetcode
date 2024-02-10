class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        for i in range(len(candies)):
            if candies[i] > max_candies:
                max_candies = candies[i]

        boolList = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                boolList.append(True)
            else:
                boolList.append(False)

        return boolList