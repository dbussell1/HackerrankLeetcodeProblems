class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:                                      
            return nums[0]

        def inner(nums):                                
            last, now = 0, 0                            
            for num in nums:
                last, now = now, max(last + num, now)   
            return now

        res1 = inner(nums[:n-1])    
        res2 = inner(nums[1:])      

        return max(res1, res2)
