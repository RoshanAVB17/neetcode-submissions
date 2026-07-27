from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        hashmap = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in hashmap:
                hashmap[key].append(i)
            else:
                hashmap[key] = [i]
        return (list(hashmap.values()))
        



