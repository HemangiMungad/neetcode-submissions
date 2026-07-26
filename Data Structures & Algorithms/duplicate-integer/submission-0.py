class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashfunc = set()

        for i in nums:
            if i in hashfunc:
                return True;
            else:
                hashfunc.add(i)

        return False;
        