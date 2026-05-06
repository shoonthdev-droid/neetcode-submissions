class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max, max_sum = 0, nums[0]
        curr_min, min_sum = 0, nums[0]

        for n in nums:
            curr_max = max(n, curr_max + n)
            max_sum = max(max_sum, curr_max)

            curr_min = min(n, curr_min + n)
            min_sum = min(curr_min, min_sum)

            total_sum += n
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)