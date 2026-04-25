class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            # store nums in the hashmap with the index
            hashmap[num] = i
        
        # hashmap = { 3: 0, 4: 1, 5: 2, 6: 3 }

        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in hashmap:
                j = hashmap[second_num]
                if i != j:
                    return [i, j]
            
        