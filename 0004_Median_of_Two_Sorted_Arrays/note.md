# Median of Two Sorted Arrays

## 题目

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

**进阶：** 你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

**示例 1：**

> 输入：nums1 = [1,3], nums2 = [2]\
> 输出：2.00000\
> 解释：合并数组 = [1,2,3] ，中位数 2

**示例 2：**

> 输入：nums1 = [1,2], nums2 = [3,4]\
> 输出：2.50000\
> 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

**示例 3：**

> 输入：nums1 = [0,0], nums2 = [0,0]
> 输出：0.00000

**示例 4：**

> 输入：nums1 = [], nums2 = [1]\
> 输出：1.00000

**示例 5：**

> 输入：nums1 = [2], nums2 = []\
> 输出：2.00000

**提示：**

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- $-10^6$ <= nums1[i], nums2[i] <= $10^6$

## 解题思路

### 方案 1

同时遍历两个集合，按从小到达插入。时间复杂度 0(m + n)。

```python
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
```

### 方案 2
