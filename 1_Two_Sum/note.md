# Two Sum

## Question

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**

> **Input:** nums = [2, 7, 11, 15], target = 9\
> **Output:** [0, 1]\
> **Output:** Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

> Input: nums = [3,2,4], target = 6\
> Output: [1,2]

**Example 3:**

> Input: nums = [3,3], target = 6\
> Output: [0,1]

**Constraints:**

- 2 <= nums.length <= $10^3$
- $-10^9$ <= nums[i] <= $10^9$
- $-10^9$ <= target <= $10^9$
- **Only one valid answer exists.**

## 解题思路

### 方案 1 - 嵌套循环

可以简单的使用嵌套循环遍历所有可能的组合，找寻出相加结果为 `target` 的组合的 `index` 即可。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums[i_index+1:]):
                if i + j == target:
                    return [i_index, j_index]
```
