class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            first_num = target - num
            if first_num in hashmap and hashmap[first_num] != i:
                return [hashmap[first_num], i]
            else:
                hashmap[num] = i
        return []
