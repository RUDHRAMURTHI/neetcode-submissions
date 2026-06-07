class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        r,c =0,0
        visit = set()
        length = 0
        queue = deque()
        queue.append((r,c))
        visit.add((r,c))
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        Rows, Columns = len(grid), len(grid[0])
        while queue:
            for i in range(len(queue)):
                (r,c) = queue.popleft()
                if r == Rows-1 and c == Columns-1:
                    return length
                for dr, dc in directions:
                    if min(r+dr, c+dc) < 0 or r+dr == Rows or c+dc == Columns or grid[r+dr][c+dc] == 1 or (r+dr, c+dc) in visit:
                        continue
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))

            length +=1
        
        return -1
                
        
        