class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        res = []
        for x in nums2:
            if x in set1 and x not in res:
                res.append(x)
        return res
        