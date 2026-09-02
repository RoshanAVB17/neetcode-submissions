class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        window = {}

        for char in t:
            countT[char] = countT.get(char,0) + 1
        left = 0
        result = [-1,-1]
        result_length = float("inf")
        have = 0
        required = len(countT)

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0) + 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            while have == required:
                window_length = right - left + 1

                if window_length < result_length:
                    result = [left,right]
                    result_length = window_length
                window[s[left]] -=1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
        return s[result[0]:result[1] + 1] if result_length != float("inf") else ""    






        
        