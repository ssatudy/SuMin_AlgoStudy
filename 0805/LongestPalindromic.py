class Solution:
    def longestPalindrome(self,s: str) -> str:
        pal = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    word = s[i:j+1]
                    if word == word[::-1]:
                        if len(pal)<len(s[i:j+1]):        
                            pal = s[i:j+1]
            if len(pal) >= len(s)-i:
                return pal
        return pal


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         for i in range(len(s))[::-1]:
#             for j in range(len(s)-i):
#                 word = s[j:j+i+1]
#                 if word == word[::-1]:
#                     return s[j:j+i+1]
            

