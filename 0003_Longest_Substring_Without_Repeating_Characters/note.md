# Longest Substring Without Repeating Characters

## 题目

给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。

**示例 1:**

> 输入: s = "abcabcbb"\
> 输出: 3 \
> 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

**示例 2:**

> 输入: s = "bbbbb"\
> 输出: 1\
> 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

**示例 3:**

> 输入: s = "pwwkew"\
> 输出: 3\
> 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是 **子串** 的长度，"pwke" 是一个子序列，不是子串。

**示例 4:**

> 输入: s = ""\
> 输出: 0

**提示：**

- 0 <= s.length <= 5 * 104
- s 由英文字母、数字、符号和空格组成

## 解题思路

### 方案 1 - 嵌套循环

使用 2 层嵌套循环，依次查询以某个字符开头的最长无重复字符子串的长度。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            char_set = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                length += 1
                char_set.add(s[j])
            if length > max_len:
                max_len = length
        return max_len
```

### 方案 2 - 滑动窗口

方案一最大的一个缺陷是忽略了一个事实：选择字符串中的第 $k$ 个字符作为起始位置，并且得到了不包含重复字符的最长子串的结束位置为 $r_k$，那么当我们选择第 $k+1$ 个字符作为起始位置时，首先从 $k+1$ 到 $r_k$ 的字符显然是不重复的。利用了这个信息后，那时间复杂度就从 $O(N^2)$ 降至 $O(N^2)$ (左右指针分别遍历一次字符串)。

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r_cur, max_len = -1, 0
        char_set = set()
        
        for l_cur in range(len(s)):
            if l_cur != 0:
                char_set.remove(s[l_cur - 1])
            
            while r_cur + 1 < len(s) and s[r_cur + 1] not in char_set:
                char_set.add(s[r_cur + 1])
                r_cur += 1
            max_len = max(max_len, r_cur - l_cur + 1)
        return max_len
```
