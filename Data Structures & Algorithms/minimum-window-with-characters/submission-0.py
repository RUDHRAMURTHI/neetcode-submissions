class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map={}
        t_map={}
        l=0
        res=""
        min_length=float("infinity")
        for char in t:
            t_map[char] = 1+t_map.get(char,0)
        have= 0
        need=len(t_map)
        # print("t_map:", t_map)
        for r in range(len(s)):
            # print("s[r]:", s[r])
            # print("window", s[l:r+1])
            if s[r] in t_map:
                s_map[s[r]]=1+s_map.get(s[r],0)
                if s_map[s[r]] == t_map[s[r]]:
                    have+=1
            # print("s_map:", s_map)
            while have == need:
                if (r-l+1) < min_length:
                    min_length = min(min_length, r-l+1)
                    res=s[l:r+1]
                    # print("res:", res)
                    # print("min_length:", min_length)
                if s[l] in t_map:
                    s_map[s[l]]-=1
                    if s_map[s[l]] < t_map[s[l]]:
                        have-=1
                l+=1
        return res
        