# https://www.interviewbit.com/problems/delete-and-conquer/


class Solution:
    # @param A : list of integers
    # @return an integer
    def deleteandconquer(self, A):
        f = {}
        b = 0
        for a in A:
            if a not in f: f[a] = 0
            f[a] += 1
            b = max(b, f[a])
        return len(A) - b
