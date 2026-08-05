class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_text = re.sub("[^a-zA-Z0-9]", "", s)

        clean_text = clean_text.lower()


        i = 0 
        j = len(clean_text)-1

        while (i<=j):
            if clean_text[i] != clean_text[j]:
                
                return False
            else: 
                i +=1
                j -=1




        return True

        