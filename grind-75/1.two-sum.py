class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, n in enumerate(nums):
            curr_target = target - n
            if curr_target in seen:
                return [seen[curr_target], idx]
            seen[n] = idx
