class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val: index 
        #hashmap, every previous element that comes before the current element is stored in the map

        for i, n in enumerate(nums):     # i = index, n = number
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
