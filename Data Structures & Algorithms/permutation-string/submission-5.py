from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l=0
        r = len(s1)
        check=[]


        for l in range(0,len(s2)-r+1):
            check.append(s2[l:l+r])

        print(check)

        for string in check:
            if Counter(string) == Counter(s1):
                return True
        
        return False




        


        