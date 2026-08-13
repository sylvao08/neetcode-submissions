class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_id = dict()
        for id, num in enumerate(nums):
            comp = target - num
            if comp in value_id.keys():
                return sorted([id, value_id[comp]])
            value_id[num]=id
            
        