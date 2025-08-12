"""
DFS Practice Problems with Solutions
These are common LeetCode problems that use DFS
"""

from typing import List, Optional
import sys
import os
# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_structures.graph import TreeNode, create_binary_tree


class DFSProblems:
    """Collection of DFS practice problems"""
    
    # ========== Problem 1: Maximum Depth of Binary Tree ==========
    # LeetCode 104: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: 3
        
        Time: O(n), Space: O(h) where h is height
        """
        if not root:
            return 0
        
        # DFS: max depth = 1 + max(left_depth, right_depth)
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
    
    # ========== Problem 2: Path Sum ==========
    # LeetCode 112: https://leetcode.com/problems/path-sum/
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Given root and targetSum, return true if tree has root-to-leaf path
        such that adding up all values equals targetSum.
        
        Example:
        Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
        Output: true (5 -> 4 -> 11 -> 2)
        
        Time: O(n), Space: O(h)
        """
        if not root:
            return False
        
        # Leaf node check
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check left and right subtrees
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))
    
    # ========== Problem 3: Number of Islands ==========
    # LeetCode 200: https://leetcode.com/problems/number-of-islands/
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid which represents a map of '1's (land) 
        and '0's (water), return the number of islands.
        
        Example:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3
        
        Time: O(m*n), Space: O(m*n) for recursion
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = 0
        
        def dfs(row: int, col: int):
            # Base cases
            if (row < 0 or row >= m or col < 0 or col >= n or 
                grid[row][col] == '0'):
                return
            
            # Mark as visited by changing to '0'
            grid[row][col] = '0'
            
            # Visit all 4 directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        # Find and count islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        
        return islands
    
    # ========== Problem 4: Generate Parentheses ==========
    # LeetCode 22: https://leetcode.com/problems/generate-parentheses/
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, generate all combinations 
        of well-formed parentheses.
        
        Example:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        
        Time: O(4^n / √n), Space: O(n)
        """
        result = []
        
        def dfs(current: str, open_count: int, close_count: int):
            # Base case: used all n pairs
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Can add open parenthesis if we haven't used n yet
            if open_count < n:
                dfs(current + '(', open_count + 1, close_count)
            
            # Can add close parenthesis if it won't make invalid
            if close_count < open_count:
                dfs(current + ')', open_count, close_count + 1)
        
        dfs('', 0, 0)
        return result
    
    # ========== Problem 5: Combination Sum ==========
    # LeetCode 39: https://leetcode.com/problems/combination-sum/
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given array of distinct integers candidates and target integer,
        return all unique combinations where chosen numbers sum to target.
        Same number may be chosen unlimited times.
        
        Example:
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        
        Time: O(N^(T/M)) where N is candidates length, T is target, M is minimal value
        Space: O(T/M)
        """
        result = []
        
        def dfs(start: int, path: List[int], remaining: int):
            # Base cases
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            # Try each candidate from start index
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Use same index i (not i+1) because we can reuse numbers
                dfs(i, path, remaining - candidates[i])
                path.pop()  # Backtrack
        
        dfs(0, [], target)
        return result
    
    # ========== Problem 6: Word Search ==========
    # LeetCode 79: https://leetcode.com/problems/word-search/
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and string word,
        return true if word exists in the grid.
        
        Example:
        Input: board = [["A","B","C","E"],
                       ["S","F","C","S"],
                       ["A","D","E","E"]], 
               word = "ABCCED"
        Output: true
        
        Time: O(m*n*4^L) where L is word length, Space: O(L)
        """
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(row: int, col: int, index: int) -> bool:
            # Found the word
            if index == len(word):
                return True
            
            # Out of bounds or wrong character
            if (row < 0 or row >= m or col < 0 or col >= n or 
                board[row][col] != word[index]):
                return False
            
            # Mark as visited by changing the character
            temp = board[row][col]
            board[row][col] = '#'
            
            # Search in 4 directions
            found = (dfs(row + 1, col, index + 1) or
                    dfs(row - 1, col, index + 1) or
                    dfs(row, col + 1, index + 1) or
                    dfs(row, col - 1, index + 1))
            
            # Backtrack
            board[row][col] = temp
            
            return found
        
        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
    
    # ========== Problem 7: Subsets ==========
    # LeetCode 78: https://leetcode.com/problems/subsets/
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums of unique elements,
        return all possible subsets (the power set).
        
        Example:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        
        Time: O(2^n), Space: O(n) for recursion
        """
        result = []
        
        def dfs(start: int, path: List[int]):
            # Add current subset
            result.append(path[:])
            
            # Generate subsets by including each remaining element
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()  # Backtrack
        
        dfs(0, [])
        return result
    
    # ========== Problem 8: Permutations ==========
    # LeetCode 46: https://leetcode.com/problems/permutations/
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, 
        return all possible permutations.
        
        Example:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        
        Time: O(n!), Space: O(n)
        """
        result = []
        
        def dfs(path: List[int], remaining: List[int]):
            # Base case: no more elements to add
            if not remaining:
                result.append(path[:])
                return
            
            # Try each remaining element
            for i in range(len(remaining)):
                # Choose element at index i
                path.append(remaining[i])
                # Recurse with remaining elements
                dfs(path, remaining[:i] + remaining[i+1:])
                # Backtrack
                path.pop()
        
        dfs([], nums)
        return result


def test_dfs_problems():
    """Test DFS problems with examples"""
    problems = DFSProblems()
    
    print("=" * 60)
    print("Testing DFS Problems")
    print("=" * 60)
    
    # Test 1: Maximum Depth
    print("\n1. Maximum Depth of Binary Tree")
    tree = create_binary_tree([3, 9, 20, None, None, 15, 7])
    result = problems.maxDepth(tree)
    print(f"   Input: [3,9,20,null,null,15,7]")
    print(f"   Output: {result}")
    print(f"   Expected: 3")
    
    # Test 2: Path Sum
    print("\n2. Path Sum")
    tree = create_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    result = problems.hasPathSum(tree, 22)
    print(f"   Target Sum: 22")
    print(f"   Output: {result}")
    print(f"   Expected: True")
    
    # Test 3: Number of Islands
    print("\n3. Number of Islands")
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = problems.numIslands([row[:] for row in grid])  # Copy to avoid modification
    print(f"   Output: {result}")
    print(f"   Expected: 3")
    
    # Test 4: Generate Parentheses
    print("\n4. Generate Parentheses")
    result = problems.generateParenthesis(3)
    print(f"   Input: n = 3")
    print(f"   Output: {result}")
    print(f"   Expected: ['((()))', '(()())', '(())()', '()(())', '()()()']")
    
    # Test 5: Combination Sum
    print("\n5. Combination Sum")
    result = problems.combinationSum([2, 3, 6, 7], 7)
    print(f"   Candidates: [2,3,6,7], Target: 7")
    print(f"   Output: {result}")
    print(f"   Expected: [[2, 2, 3], [7]]")
    
    # Test 6: Word Search
    print("\n6. Word Search")
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    result = problems.exist(board, "ABCCED")
    print(f"   Word: 'ABCCED'")
    print(f"   Output: {result}")
    print(f"   Expected: True")
    
    # Test 7: Subsets
    print("\n7. Subsets")
    result = problems.subsets([1, 2, 3])
    print(f"   Input: [1,2,3]")
    print(f"   Output: {result}")
    print(f"   Number of subsets: {len(result)} (Expected: 8)")
    
    # Test 8: Permutations
    print("\n8. Permutations")
    result = problems.permute([1, 2, 3])
    print(f"   Input: [1,2,3]")
    print(f"   Output: {result}")
    print(f"   Number of permutations: {len(result)} (Expected: 6)")


if __name__ == "__main__":
    test_dfs_problems()