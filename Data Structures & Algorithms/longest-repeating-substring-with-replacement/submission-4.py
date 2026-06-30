class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # res=0
        # for i in range(len(s)):
        #     # print("start:",s[i])
        #     count={}
        #     max_f=0
        #     for j in range(i, len(s)):
        #         count[s[j]]=1+count.get(s[j], 0)
        #         max_f=max(max_f, count[s[j]])
        #         if (j-i+1)-max_f<=k:
        #             # print("length:", j-i+1)
        #             res=max(res, j-i+1)
        # return res

        # res = 0
        # l=0
        # count={}
        # for r in range(len(s)):
        #     # print("curr:", s[r])
        #     # print("l, r:", l,r)
        #     count[s[r]] = 1+count.get(s[r],0)
        #     while (r-l+1)-max(count.values())>k:
        #         # print("length:", r-l+1)
        #         count[s[l]]-=1
        #         l+=1
        #     res=max(res, r-l+1)
        #     # print("res:", res)
        # return res

        res = 0
        l=0
        count={}
        max_f=0
        for r in range(len(s)):
            # print("curr:", s[r])
            # print("l, r:", l,r)
            count[s[r]] = 1+count.get(s[r],0)
            max_f=max(max_f,count[s[r]])
            while (r-l+1)-max_f>k:
                # print("length:", r-l+1)
                count[s[l]]-=1
                l+=1
            res=max(res, r-l+1)
            # print("res:", res)
        return res

        