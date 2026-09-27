class Solution:
    def hammingWeight(self, n: int) -> int:

        count=0

        num_binary = bin(n)[2:]

        num_str = str(num_binary)

        for i in num_str:
            if i=="1":
                count +=1
        
        return count

        