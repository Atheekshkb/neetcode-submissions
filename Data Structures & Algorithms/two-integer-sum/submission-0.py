class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, nums in enumerate(nums):
            ans = target - nums
            if ans in seen:
                return [seen[ans], i]
            seen[nums] = i
        return []