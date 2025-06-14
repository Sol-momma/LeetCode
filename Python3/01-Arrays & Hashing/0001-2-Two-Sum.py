class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #ハッシュテーブルを作る
        indices=dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices:
                return [indices[diff],i]
            indices [nums[i]] = i
