class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        item_set = set(nums)
        dup = True if len(item_set) < len(nums) else False
        return dup