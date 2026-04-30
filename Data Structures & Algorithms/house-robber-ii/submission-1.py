class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.help(nums[1:]), self.help(nums[:-1]))
    def help(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2