class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() ## Initialize an empty set to track seen numbers
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
