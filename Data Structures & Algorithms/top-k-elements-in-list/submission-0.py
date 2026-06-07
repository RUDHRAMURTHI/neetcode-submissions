class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map=defaultdict(int)
        for num in nums:
            map[num]+=1
        # print("map:", map)
        pair=[]
        for key, value in map.items():
            pair.append((value, key))
        # print("pair:", pair)
        pair.sort(reverse=True)
        # print("pair:", pair)
        return [pair[i][1] for i in range(k)]
