class Solution:
    # Solution 1
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     max_len = 0
    #     for i in range(len(s)):
    #         char_set = set()
    #         length = 0
    #         for j in range(i, len(s)):
    #             if s[j] in char_set:
    #                 break
    #             length += 1
    #             char_set.add(s[j])
    #         if length > max_len:
    #             max_len = length
    #     return max_len

    # Solution 2
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     r_cur, max_len = -1, 0
    #     char_set = set()
        
    #     for l_cur in range(len(s)):
    #         if l_cur != 0:
    #             char_set.remove(s[l_cur - 1])   # 每次循环开始, 去除 set 里面的上一起始位置的元素
            
    #         while r_cur + 1 < len(s) and s[r_cur + 1] not in char_set:
    #             # 当右指针下一位置所在的元素没出现过时，右指针右移到此位置
    #             char_set.add(s[r_cur + 1])
    #             r_cur += 1
    #         # 当开始出现重复字符时，更新最大长度的值
    #         max_len = max(max_len, r_cur - l_cur + 1)
    #     return max_len

    # Solution 3
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_cur, max_len, char_dict = -1, 0, {}
        for index, char in enumerate(s): 
            # 如果当前字符已经出现过，且出现的位置是在起始下标之后，则说明当前子串出现了重复字符，将起始下标更新到重复位置
            if char in char_dict and char_dict[char] > start_cur:
                start_cur = char_dict[char]
                char_dict[char] = index
            else:
                char_dict[char] = index
                max_len = max(max_len, index - start_cur)
        return max_len

if __name__ == "__main__":
    solution = Solution()
    res = solution.lengthOfLongestSubstring(s='abcdefadfweasdfwe')
    print(res)