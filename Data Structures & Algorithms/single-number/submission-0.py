class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        stack = {}
        
        for i in nums:
            if i not in stack:
                stack[i] = 1
            else:
                stack[i] = stack[i] + 1

        
        for key,value in stack.items():
            if value ==1:
                return key

            
