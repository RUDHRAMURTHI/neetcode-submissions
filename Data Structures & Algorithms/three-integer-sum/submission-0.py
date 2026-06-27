class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print("nums:", nums)
        res=[]
        for i in range(len(nums)):
            num1 = nums[i]
            l=i+1
            r=len(nums)-1
            target = 0-num1
            # print("target:", target)
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    out=[num1,nums[l], nums[r]]
                    if out not in res:
                        res.append(out)
                    l+=1
        # print("res:", res)
        return res
                



        