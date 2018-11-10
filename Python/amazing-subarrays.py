# https://www.interviewbit.com/problems/amazing-subarrays/


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(A)

        substrings = 0
        for i in range(n):
            if A[i] in vowels:
                substrings = (substrings + n - i) % 10003
        return substrings % 10003
