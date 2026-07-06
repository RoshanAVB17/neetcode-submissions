class Solution:
    def topKFrequent(self, nums, k):

        # Step 1: Count frequency
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        # Step 2: Create empty buckets
        freq = []

        for i in range(len(nums) + 1):
            freq.append([])

        # Step 3: Put numbers into buckets
        for n in count:
            c = count[n]
            freq[c].append(n)

        # Step 4: Collect answer
        res = []

        i = len(freq) - 1

        while i > 0:

            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res

            i -= 1