// Problem link: https://leetcode.com/problems/next-greater-element-i/
// Best solution explanation: https://youtu.be/mJWQjJpEMa4?si=or1uLOznW8NZUDnf

// Solution 1:
// Complexity: O(n+m)

var nextGreaterElement = function (nums1, nums2) {
  const nextGreater = {};
  const stack = [];

  // Iterate through nums2 to find the next greater element for each number
  for (const num of nums2) {
    while (stack.length && num > stack[stack.length - 1]) {
      nextGreater[stack.pop()] = num;
    }
    stack.push(num);
  }

  // Iterate through nums1 to build the result array
  const result = nums1.map((num) => nextGreater[num] || -1);

  return result;
};

// Example usage
const nums1 = [4, 1, 2];
const nums2 = [1, 3, 4, 2];
const result = nextGreaterElement(nums1, nums2);
console.log(result);
