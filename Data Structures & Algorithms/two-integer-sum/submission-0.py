class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       storage = {}
       for i , n in enumerate (nums):
            diff = target - n
            if diff in storage:
                return [storage[diff], i]

            storage[n] = i
        