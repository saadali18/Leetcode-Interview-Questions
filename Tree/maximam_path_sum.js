// Leetcode Problem: Binary Tree Maximum Path Sum (https://leetcode.com/problems/binary-tree-maximum-path-sum/)

/*
The LeetCode problem "Binary Tree Maximum Path Sum" is asking for the maximum sum that can be obtained by traversing any non-empty path in a binary tree. Here are the key points of the problem:

Objective: The goal is to find the maximum path sum among all possible paths in the given tree. The path can start and end at any node in the tree.

The problem is asking us to find the maximum sum achievable by traversing any path in the binary tree. The solution needs to explore and compare various paths in a systematic way to determine the maximum sum. The recursive approach used in the provided solution effectively explores the tree and calculates the maximum sum dynamically.

Time Complexity: O(n)
Recursive Calls: The dfs function is called for each node once, and it performs constant time operations at each call. Therefore, the time complexity of the recursive part is O(n).

Space Complexity: O(n)
Recursion Stack: The space complexity is determined by the maximum depth of the recursion stack. In the worst case, the recursion stack could go as deep as n (for a skewed tree). Therefore, the space complexity due to the recursion stack is O(n).
Other Variables: Apart from the recursion stack, the algorithm uses a constant amount of space for variables like maxSum, left, right. Hence, the space complexity for these variables is O(1).

The overall space complexity is O(n) due to the recursion stack. The time complexity is O(n), as each node is visited once during the recursive traversal. The solution is efficient in terms of time and space complexity. The recursive approach allows the algorithm to explore all nodes in a depth-first manner while keeping track of the maximum path sum dynamically.

Approach: The provided code addresses the "Binary Tree Maximum Path Sum" problem using a recursive Depth-First Search (DFS) approach. The function maxPathSum initializes a variable maxSum to track the maximum path sum throughout the traversal. The recursive function dfs calculates the maximum path sum for each node by considering both left and right subtrees. The base case ensures that null nodes return 0, signifying an absence of a path. The Math.max(0, ...) is used to handle negative values, allowing the algorithm to exclude negative contributions to the path sum. The global maxSum is updated whenever a new maximum path sum is encountered. The approach efficiently explores the binary tree, dynamically updating the maximum sum, and returns the final result after the traversal.
*/

function maxPathSum(root) {
  let maxSum = Number.MIN_SAFE_INTEGER;

  function dfs(node) {
    if (!node) return 0;
    let left = Math.max(0, dfs(node.left));
    let right = Math.max(0, dfs(node.right));
    maxSum = Math.max(maxSum, left + right + node.val);
    return Math.max(left, right) + node.val;
  }

  dfs(root);

  return maxSum;
}
