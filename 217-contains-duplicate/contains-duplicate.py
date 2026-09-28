class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #return len(nums) != len(set(nums))
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False