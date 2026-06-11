class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        product = 1
        for i in range(len(nums)):
            prefix[i] = product
            product*=nums[i]
        suf_product=1
        for j in range(len(nums)-1,-1,-1):
            suffix[j]=prefix[j]*suf_product
            suf_product*=nums[j]
        return suffix

        