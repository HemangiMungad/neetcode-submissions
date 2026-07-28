class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        nums_set = set(nums)

        for n in nums_set :
            if n-1 not in nums_set:
                crnt_len = 0
                crnt_num = n
                while crnt_num in nums_set:
                    crnt_len += 1
                    crnt_num += 1
                res = max(res,crnt_len)

        return res


        