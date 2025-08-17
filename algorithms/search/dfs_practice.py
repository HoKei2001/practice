class Stack:
    def __init__(self) -> None:
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.pop()
    
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


def dfs(graph, start):
    visited = set()  # 记录已经访问过的节点 初始化为空集合
    visited.add(start)
    stack = Stack()  # 初始化栈，将起始节点加入栈
    stack.push(start)
    while not stack.is_empty():  # 栈不为空时，继续遍历
        vertex = stack.pop()  # 从栈中取出第一个节点
        print(vertex)  # 打印当前节点
        for neighbor in graph.adjacency_list[vertex]:  # 遍历当前节点的所有邻居
            if neighbor not in visited:  # 如果邻居节点未被访问过
                visited.add(neighbor)  # 标记为已访问
                stack.push(neighbor)  # 将邻居节点加入栈


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.adjacency_list[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
# 为什么dfs可以用递归实现，但是bfs不行？
# 因为递归本身就是栈的逻辑，但是bfs是队列的逻辑，而队列是显式的，需要手动实现
# 这里“显式的逻辑”指的是，队列的数据结构不像递归那样由程序调用栈自动维护，而是需要我们在代码中手动创建和操作队列（如 list、deque 等），来实现 BFS 的遍历顺序。


if __name__ == "__main__":
    print("-----stack-----")
    dfs(graph, 0)
    print("-----recursive-----")
    dfs_recursive(graph, 0)
    # dfs的栈实现和递归实现两种方法的输出结果不一样，为什么？
    # 答：这是正常的！两种实现都是正确的DFS，只是遍历顺序不同：
    # 1. 迭代版本：使用栈(LIFO)，后加入的邻居先处理
    # 2. 递归版本：按邻接表顺序依次递归处理邻居
    # 两种都保证了深度优先，但具体路径可能不同
