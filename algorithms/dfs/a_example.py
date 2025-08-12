import sys
import os
# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from data_structures.graph import Graph
from collections import deque


graph = Graph()
graph.add_edges([[0, 1], [0, 2], [1, 0], [1,3], [2, 0], [2, 3],[3,1],[3,2],[3,4],[4,3]])

def dfs(graph, start):
    visited = set()  # 记录已经访问过的节点 初始化为空集合
    visited.add(start)
    stack = deque([start]) # 初始化栈，将起始节点加入栈
    while stack: # 栈不为空时，继续遍历
        vertex = stack.pop() # 从栈中取出第一个节点
        print(vertex) # 打印当前节点
        for neighbor in graph.adjacency_list[vertex]:  # 遍历当前节点的所有邻居
            if neighbor not in visited: # 如果邻居节点未被访问过
                visited.add(neighbor)  # 标记为已访问
                stack.append(neighbor) # 将邻居节点加入栈


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.adjacency_list[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

if __name__ == "__main__":
    # dfs(graph, 0)  # 从节点0开始遍历
    # print("--------------------------------")
    dfs_recursive(graph, 0)  # 从节点0开始遍历