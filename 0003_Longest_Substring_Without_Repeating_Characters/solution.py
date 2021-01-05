class Solution:
    # 第一次解法，双重循环嵌套
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

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     pass


if __name__ == "__main__":
    solution = Solution()
    res = solution.lengthOfLongestSubstring(s='abcdefadfweasdfwe')
    print(res)