class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p1 = 0
        if (len(nums) == 1):
            return

        while (p1 < len(nums) and p0 < len(nums)):
            # swap
            if (nums[p0] == 0 and nums[p1] != 0):
                if (p1 < p0):
                    p1 += 1
                else:
                    nums[p0], nums[p1] = nums[p1], nums[p0]

            # no swap
            if (nums[p0] != 0):
                p0 += 1
            if (nums[p1] == 0):
                p1 += 1
