"""
Common graph data structures for LeetCode practice
"""

from typing import List, Optional, Dict, Set
from collections import defaultdict, deque


class TreeNode:
    """Binary tree node - commonly used in LeetCode problems"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"
    
    @staticmethod
    def from_list(vals: List[Optional[int]]) -> Optional['TreeNode']:
        """Create a binary tree from level-order list representation"""
        if not vals:
            return None
        
        root = TreeNode(vals[0])
        queue = deque([root])
        i = 1
        
        while queue and i < len(vals):
            node = queue.popleft()
            
            # Add left child
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            
            # Add right child
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def to_list(self) -> List[Optional[int]]:
        """Convert tree to level-order list representation"""
        if not self:
            return []
        
        result = []
        queue = deque([self])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        
        return result


class ListNode:
    """Linked list node - commonly used in LeetCode problems"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"
    
    @staticmethod
    def from_list(vals: List[int]) -> Optional['ListNode']:
        """Create a linked list from a list of values"""
        if not vals:
            return None
        
        dummy = ListNode(0)
        curr = dummy
        
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next
    
    def to_list(self) -> List[int]:
        """Convert linked list to Python list"""
        result = []
        curr = self
        
        while curr:
            result.append(curr.val)
            curr = curr.next
        
        return result


class Graph:
    """
    Graph representation with common operations
    Supports both adjacency list and matrix representations
    """
    
    def __init__(self, directed: bool = False):
        self.adjacency_list: Dict[int, List[int]] = defaultdict(list)
        self.directed = directed
        self.vertices: Set[int] = set()
    
    def add_edge(self, u: int, v: int, weight: int = 1):
        """Add an edge to the graph"""
        self.adjacency_list[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
        
        if not self.directed:
            self.adjacency_list[v].append(u)
    
    def add_edges(self, edges: List[List[int]]):
        """Add multiple edges from a list"""
        for edge in edges:
            if len(edge) == 2:
                self.add_edge(edge[0], edge[1])
            elif len(edge) == 3:
                self.add_edge(edge[0], edge[1], edge[2])
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """Get all neighbors of a vertex"""
        return self.adjacency_list[vertex]
    
    def to_adjacency_matrix(self, n: int = None) -> List[List[int]]:
        """Convert to adjacency matrix representation"""
        if n is None:
            n = max(self.vertices) + 1 if self.vertices else 0
        
        matrix = [[0] * n for _ in range(n)]
        
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                matrix[u][v] = 1
        
        return matrix
    
    @staticmethod
    def from_adjacency_matrix(matrix: List[List[int]], directed: bool = False) -> 'Graph':
        """Create a graph from adjacency matrix"""
        graph = Graph(directed=directed)
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j]:
                    if directed or i <= j:  # Avoid duplicate edges in undirected graph
                        graph.add_edge(i, j, matrix[i][j])
        
        return graph
    
    def __repr__(self):
        return f"Graph(vertices={sorted(self.vertices)}, directed={self.directed})"
    
    def display(self):
        """Display the graph structure"""
        print(f"Graph (directed={self.directed}):")
        for vertex in sorted(self.vertices):
            neighbors = self.adjacency_list[vertex]
            print(f"  {vertex} -> {neighbors}")


# Helper functions for creating test cases
def create_binary_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to create binary tree from list"""
    return TreeNode.from_list(vals)


def create_linked_list(vals: List[int]) -> Optional[ListNode]:
    """Helper function to create linked list from list"""
    return ListNode.from_list(vals)


def create_graph(edges: List[List[int]], directed: bool = False) -> Graph:
    """Helper function to create graph from edge list"""
    graph = Graph(directed=directed)
    graph.add_edges(edges)
    return graph