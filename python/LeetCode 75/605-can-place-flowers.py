class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0
        if (len(flowerbed) < 2):
            if (flowerbed[0] == 0):
                flowerbed[0] = 1
                possible += 1

        if (flowerbed[0] == 0 and flowerbed[1] == 0):
            flowerbed[0] = 1
            possible += 1

        if (flowerbed[len(flowerbed) - 2] == 0 and flowerbed[len(flowerbed) - 1] == 0):
            flowerbed[len(flowerbed) - 1] = 1
            possible += 1

        for i in range(1, len(flowerbed) - 2):
            if (flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                possible += 1

        return possible >= n