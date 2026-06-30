class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            # print("start:",s[i])
            count={}
            max_f=0
            for j in range(i, len(s)):
                count[s[j]]=1+count.get(s[j], 0)
                max_f=max(max_f, count[s[j]])
                if (j-i+1)-max_f<=k:
                    # print("length:", j-i+1)
                    res=max(res, j-i+1)
        return res
        