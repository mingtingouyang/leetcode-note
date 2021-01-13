from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        cur_1, cur_2 = 0, 0
        while cur_1 < len(nums1) and cur_2 < len(nums2):
            if nums1[cur_1] < nums2[cur_2]:
                nums.append(nums1[cur_1])
                cur_1 += 1
            else:
                nums.append(nums2[cur_2])
                cur_2 += 1
        nums += (nums1[cur_1:]) if cur_1 < len(nums1) else (nums2[cur_2:])

        if len(nums) % 2 == 1 :
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2


if __name__ == "__main__":
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2])
    print(result)