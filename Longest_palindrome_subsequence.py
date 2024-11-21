#Dynamic Programming (Bottom up Approach)
class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        
        # Use a 1D array to store the subproblem results
        store = [0] * n

        for i in range(n - 1, -1, -1):
            new_store = [0] * n
            new_store[i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    new_store[j] = store[j - 1] + 2
                else:
                    new_store[j] = max(new_store[j - 1], store[j])

            store = new_store
        
        # The length of the longest palindromic subsequence in the entire string
        return store[n - 1]

# Example usage
s1 = "bbbab"
sol = Solution()
print(sol.longestPalindromeSubseq(s1))
