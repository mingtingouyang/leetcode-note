# Two Sum

## 题目

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

**示例 1：**

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

**示例 2：**

输入：nums = [3,2,4], target = 6
输出：[1,2]

**示例 3：**

输入：nums = [3,3], target = 6
输出：[0,1]

**提示：**

- 2 <= nums.length <= $10^3$
- $-10^9$ <= nums[i] <= $10^9$
- $-10^9$ <= target <= $10^9$
- **只会存在一个有效答案**

## 解题思路

### 方案 1 - 嵌套循环

由题意可知，仅有一种组合满足要求，所以可以简单的使用嵌套循环遍历所有可能的组合，找寻出相加结果为 `target` 的组合的 `index` 即可。

> 时间复杂度为 $O(N^2)$

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums[i_index+1:]):
                if i + j == target:
                    return [i_index, j_index]
        
        return []
```

### 方案 2 - 使用哈希表

因为题目告诉我们必定有一组元素的和为 `target`，因此我们可以转换一种思路：将 “遍历存在元素 `A` 的所有组合并判断是否满足要求” 修改成 “查找 `target - A` 是否存在”。这样的话我们就只需要一层循环即可。

> 时间复杂度 $O(N)$

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for index, num in enumerate(nums):
            if (target - num) in num_map:
                return [num_map[target - num], index]
            else:
                num_map[num] = index
        
        return []
```
