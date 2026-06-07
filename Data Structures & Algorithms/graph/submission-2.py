class Graph:
    
    def __init__(self):
        self.adjList ={}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True

    # def hasPath(self, src: int, dst: int) -> bool:
    #     visited = set()
    #     return self.dfs(src, dst, visited)

    # def dfs(self, src, dst, visited):
    #     if src == dst:
    #         return True
    #     visited.add(src)
    #     for neighbour in self.adjList.get(src, set()):
    #         if neighbour not in visited:
    #             if self.dfs(neighbour, dst, visited):
    #                 return True
    #     return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque()
        queue.append(src)
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            visited.add(curr)
            for neighbour in self.adjList.get(curr, set()):
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        return False

            
        

