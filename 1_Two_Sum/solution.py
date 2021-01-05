from typing import List


class Solution:
    # Solution 1
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i_index, i in enumerate(nums):
    #         for j_index, j in enumerate(nums[i_index+1:]):
    #             if i + j == target:
    #                 return [i_index, j_index]

    # Solution 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    res = solution.twoSum(nums=[2, 7, 11, 15], target=9)
    print(res)