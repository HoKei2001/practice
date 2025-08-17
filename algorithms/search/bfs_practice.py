
class Queue:
    def __init__(self) -> None:
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.pop(0)
    
    def is_empty(self):
        return len(self._data) == 0

class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_edges(self, edges):
        for edge in edges:
            if edge[0] not in self.adjacency_list:
                self.adjacency_list[edge[0]] = []
            self.adjacency_list[edge[0]].append(edge[1])
            if edge[1] not in self.adjacency_list:
                self.adjacency_list[edge[1]] = []
            self.adjacency_list[edge[1]].append(edge[0])

graph = Graph()
graph.add_edges(
    [[0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 1], [3, 2], [3, 4], [4, 3]]
)


def bfs(graph, start):
    visited = set()  # 记录已经访问过的节点 初始化为空集合
    visited.add(start)
    queue = Queue()  # 初始化队列，将起始节点加入队列
    queue.push(start)
    while not queue.is_empty():  # 队列不为空时，继续遍历
        vertex = queue.pop()  # 从队列中取出第一个节点
        print(vertex)  # 打印当前节点
        for neighbor in graph.adjacency_list[vertex]:  # 遍历当前节点的所有邻居
            if neighbor not in visited:  # 如果邻居节点未被访问过
                visited.add(neighbor)  # 标记为已访问
                queue.push(neighbor)  # 将邻居节点加入队列


if __name__ == "__main__":
    bfs(graph, 0)  # 从节点0开始遍历
