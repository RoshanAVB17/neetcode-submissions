class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS , countT = {} , {}

        for i in s:
            countS[i] = countS.get(i,0) + 1
        for j in t:
            countT[j] = countT.get(j,0) + 1
        
        if countT != countS:
            return False
        return True

        
        
            
            