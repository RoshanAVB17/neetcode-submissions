class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)
        longest = 0

        for n in numsSet:

            # Start only if there is no previous number
            if (n - 1) not in numsSet:

                length = 1

                # Keep checking the next number
                while (n + length) in numsSet:
                    length += 1

                # Store the maximum sequence length found so far
                longest = max(longest, length)

        return longest