# https://www.interviewbit.com/problems/scores/


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def calc_scores(self, ai, bi, an, bn):
        sa = 2 * ai + 3 * (an - ai)
        sb = 2 * bi + 3 * (bn - bi)
        return sa, sb, sa - sb

    def update_scores(self, best, ai, bi, an, bn):
        ba, bb, bd = best
        na, nb, nd = self.calc_scores(ai, bi, an, bn)
        if nd > bd:
            ba, bb, bd = na, nb, nd
        elif nd == bd and na > ba:
            ba, bb, bd = na, nb, nd
        return [ba, bb, bd]

    def solve(self, A, B):
        A.sort()
        B.sort()
        an, bn = len(A), len(B)
        ai, bi, d = 0, 0, 0
        best = self.update_scores([-float('inf')] * 3, ai, bi, an, bn)

        while ai != an or bi != bn:
            while bi < bn and B[bi] <= d + 1:
                bi += 1

            while ai < an and A[ai] <= d + 1:
                ai += 1

            if ai == an and bi == bn: break
            elif ai == an: d = B[bi] - 1
            elif bi == bn: d = A[ai] - 1
            else: d = min(A[ai], B[bi]) - 1
            best = self.update_scores(best, ai, bi, an, bn)

        best = self.update_scores(best, ai, bi, an, bn)

        return best[0], best[1]
