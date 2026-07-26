class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False;

        char_cnt = {}

        for i in s:
            char_cnt[i] = char_cnt.get(i,0)+1
        
        for i in t:
            if i not in char_cnt:
                 return False;
            else:
                if char_cnt[i] ==0:
                    return False;
                else:
                    char_cnt[i] -=1
  
        return True;       
        


        