class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = ""
        for i in range(len(strs[0])):  # ilk string uzunluğu kadar döneceğiz
            current_char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    return prefix
            prefix += current_char
        return prefix
