class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = set()
        for i in nums:
            if i in storage:
                return True
            storage.add(i)
        return False