//Base Algo is Dynamic Programing and approach is greedy approach.
//At ech step we are considering local maxima rather than looking at whole array

public class Solution {
    public int findSubarraySum(int[] a, int n) {
        int sum = 0;
        int maxi = a[0];

        for (int i = 0; i < n; i++) {
            sum += a[i];
            maxi = Math.max(maxi, sum);

            if (sum < 0) {
                sum = 0;
            }
        }
        return maxi;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] array = {-2, -3, 4, -1, -2, 1, 5, -3};
        int result = solution.findSubarraySum(array, array.length);
        System.out.println("Maximum subarray sum: " + result);
    }
}
