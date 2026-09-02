class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        window = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have = 0
        required = len(countT)
        result = [-1, -1]
        result_length = float("inf")
        left = 0

        for right in range(len(s)):

            # ADD character entering from right
            window[s[right]] = window.get(s[right], 0) + 1

            # Check requirement
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            # IMPORTANT: this is INSIDE the for loop
            while have == required:

                window_length = right - left + 1

                if window_length < result_length:
                    result = [left, right]
                    result_length = window_length

                left_char = s[left]
                window[left_char] -= 1

                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1

                # Move left AFTER removing the character
                left += 1

        return s[result[0]:result[1] + 1] if result_length != float("inf") else ""