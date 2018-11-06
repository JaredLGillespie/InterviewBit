import sys
sys.setrecursionlimit(5000)

max_depth = 0

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def calc_combs(self, L1, C1, L2, C2, memo):
        return C1 * C2 * self.fact(L1 + L2, memo) // (self.fact(L1, memo) * self.fact(L2, memo))

    def fact(self, n, memo):
        global max_depth
        max_depth += 1
        if n in memo: return memo[n]
        if n <= 1: return 1
        v = self.fact(n - 1, memo) * n
        memo[n] = v
        return v

    def solve(self, A, B):
        if not B: return 0
        mod = 1000000007
        memo = {}
        B = sorted(B)

        # 1...B[0] has 1 possible placements of length B[0] - 1
        length, combinations = B[0] - 1, 1

        for i in range(1, len(B)):
            if B[i - 1] == B[i]: continue
            if B[i - 1] + 1 == B[i]: continue
            l = (B[i] - B[i - 1] - 1) % mod
            c = (1 << (l - 1)) % mod
            combinations = self.calc_combs(length, combinations, l, c, memo) % mod
            length += l

        # B[-1]...A has 1 possible placements of length A - B[-1]
        return self.calc_combs(length, combinations, A - B[-1], 1, memo) % mod
