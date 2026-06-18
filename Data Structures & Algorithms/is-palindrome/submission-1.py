class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = [char.lower() for char in s if char.isalnum()]
        l,r=0,len(s_clean)-1
        while l<r:
            if s_clean[l] != s_clean[r]:
                return False
            l+=1
            r-=1
        return True
        