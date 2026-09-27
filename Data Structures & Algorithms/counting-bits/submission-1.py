class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []

        while n!=-1:
            count =0
            m = n

            while m:
                m = m & (m-1)
                count +=1

            res.append(count)

            n-=1

        return res[::-1]


        