class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}
        num = len(nums)

        for i in range(num):
            second = target - nums[i]
            if second in hash:
                return [hash[second],i]
            else:
                hash[nums[i]]=i

        return []