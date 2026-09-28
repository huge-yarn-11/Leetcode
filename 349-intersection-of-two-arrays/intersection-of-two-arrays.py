class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s = set()
        for num in nums1:
            if num in nums2:
                s.add(num)
        return list(s)