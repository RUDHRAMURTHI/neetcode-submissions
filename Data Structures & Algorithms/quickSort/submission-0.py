# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickSortHelper(nums, s, e):
            # print("s,e:",s,e)
            # print("nums:", [i.key for i in nums])
            #base case
            if e-s+1 <= 1:
                return nums
            
            pivot = e
            left = s
            for i in range(s, e):
                if nums[i].key<nums[pivot].key:
                    temp = nums[left]
                    nums[left] = nums[i]
                    nums[i] = temp
                    left+=1
            temp = nums[left]
            nums[left] = nums[pivot]
            nums[pivot] = temp

            quickSortHelper(nums, s, left-1)

            quickSortHelper(nums, left+1, e)

            return nums

        s = 0
        e = len(pairs) -1
        res = quickSortHelper(pairs, s, e)

        return res

        