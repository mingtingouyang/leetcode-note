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

