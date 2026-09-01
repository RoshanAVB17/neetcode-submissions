class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_count = {}
        window_count = {}

        # Count characters in s1
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        # Sliding window through s2
        for right in range(len(s2)):
            # Add current character
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # Shrink window if it becomes larger than s1
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1

                # Remove key if frequency becomes 0
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1

            # Check if both frequency maps match
            if s1_count == window_count:
                return True

        return False