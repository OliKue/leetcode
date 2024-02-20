class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Dict = set()
        for i in nums1:
            nums1Dict.add(i)

        nums2Dict = set()
        for i in nums2:
            nums2Dict.add(i)

        answer1 = nums1Dict.difference(nums2Dict)
        answer2 = nums2Dict.difference(nums1Dict)

        return [list(answer1), list(answer2)]
