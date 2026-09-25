class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s=""
        res = []


        for i in digits:
            s = s+str(i)

        value = int(s)+1

        value_s = str(value)

        for i in value_s:
            res.append(i)

        return res

        