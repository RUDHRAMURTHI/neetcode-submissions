class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        left_product=1
        for i in range(len(nums)):
            right_product=1
            for j in range(i+1,len(nums)):
                right_product = right_product*nums[j]
            res.append(left_product*right_product)
            left_product*=nums[i]
        return res
        