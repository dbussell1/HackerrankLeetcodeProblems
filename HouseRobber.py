class Solution:
	def rob(self, nums: List[int]) -> int:
		if len(nums) < 2: return nums[0]
		elif len(nums) < 3: return nums[1] if nums[0] < nums[1] else nums[0]
		elif len(nums) < 4: return nums[0] + nums[2] if nums[1] < nums[0] + nums[2] else nums[1]

		nums[2] += nums[0]

		for i in range(3, len(nums)):
			nums[i] += max(nums[i - 3], nums[i - 2])

		return nums[-1] if nums[-2] < nums[-1] else nums[-2]
