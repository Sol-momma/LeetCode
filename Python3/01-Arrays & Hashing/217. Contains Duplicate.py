class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        box = set()

        for n in nums:
            if n in box:
                return True
            box.add(n)

        return False
