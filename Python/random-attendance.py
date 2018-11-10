# https://www.interviewbit.com/problems/random-attendance/


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        return [self.find_position(A, x) for x in B]

    def find_position(self, A, x):
        position, x = 1, x - 1
        while x > 0:
            count = self.count(A, position)
            if count <= x:
                position += 1
                x -= count
            else:
                position *= 10
                x -= 1
        return position

    def count(self, A, x):
        step, x1, x2 = 0, x, x + 1
        while x1 <= A:
            step += min(A + 1, x2) - x1
            x1 *= 10
            x2 *= 10
        return step
