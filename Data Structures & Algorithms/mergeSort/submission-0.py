# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def divide(arr, s, e):
            if e-s+1 <=1:
                return arr
            m = s+((e-s)//2)
            divide(arr, s, m)
            divide(arr, m+1, e)
            merge(arr,s,m,e)
            return arr
        def merge(arr, s,m,e):
            l=arr[s:m+1]
            r=arr[m+1:e+1]
            i=0
            j=0
            k=s
            while i < len(l) and j< len(r):
                if l[i].key <= r[j].key:
                    arr[k] = l[i]
                    i+=1
                else:
                    arr[k] = r[j]
                    j+=1
                k+=1
            while i<len(l):
                arr[k] = l[i]
                i+=1
                k+=1
            while j<len(r):
                arr[k] = r[j]
                j+=1
                k+=1

            return arr
        
        s = 0
        e = len(pairs)-1
        arr = divide(pairs, s,e)
        return arr