from typing import List


class Solution:
    # Solution 1
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i_index, i in enumerate(nums):
    #         for j_index, j in enumerate(nums[i_index+1:]):
    #             if i + j == target:
    #                 return [i_index, j_index]
    #         return []

    # Solution 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for index, num in enumerate(nums):
            if (target - num) in num_map:
                return [num_map[target - num], index]
            else:
                num_map[num] = index
        
        return []


if __name__ == "__main__":
    solution = Solution()
    res = solution.twoSum(nums=[2, 7, 11, 15], target=9)
    print(res)