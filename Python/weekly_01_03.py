import math


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def bucket_base(self, size, bucket_memo):
        if size in bucket_memo: return bucket_memo[size]
        ns = size

        n = 0
        while size > 0:
            n += size
            size //= 10
        bucket_memo[ns] = n

        return n

    def find_digit(self, index, digit_offset, e, d, r, bucket_memo):
        current_digit = digit_offset
        accum_index = 0

        b = self.bucket_base(e, bucket_memo)
        for i in range(d - digit_offset):
            next_accum_index = accum_index + b
            if next_accum_index > index or next_accum_index == accum_index:
                return current_digit, accum_index
            accum_index = next_accum_index
            current_digit += 1

        next_accum_index = accum_index + r + self.bucket_base(e // 10, bucket_memo) + 1
        if next_accum_index > index or next_accum_index == accum_index:
            return current_digit, accum_index
        accum_index = next_accum_index
        current_digit += 1

        a = b - e
        for i in range(d + 1 - digit_offset, 10 - digit_offset):
            next_accum_index = accum_index + a
            if next_accum_index > index or next_accum_index == accum_index:
                return current_digit, accum_index
            accum_index = next_accum_index
            current_digit += 1

        return current_digit, accum_index

    def find_digit_single(self, index, digit_offset, bucket_memo, e=1):
        current_digit = digit_offset
        accum_index = 0

        b = self.bucket_base(e, bucket_memo)
        for i in range(10 - digit_offset):
            next_accum_index = accum_index + b
            if next_accum_index > index or next_accum_index == accum_index:
                return current_digit, accum_index
            accum_index = next_accum_index
            current_digit += 1

        return current_digit, accum_index

    def find_digit_zeroes(self, index, num_students, digit_offset, e, carry_zeroes, bucket_memo):
        current_digit = digit_offset
        accum_index = 0

        b = self.bucket_base(e // 10, bucket_memo)
        for i in range(num_students + 1 - digit_offset):
            if i == 0: next_accum_index = carry_zeroes
            else: next_accum_index = accum_index + b
            if next_accum_index > index or next_accum_index == accum_index:
                return current_digit, accum_index
            accum_index = next_accum_index
            current_digit += 1

        return current_digit, accum_index

    def find_student(self, index, num_students, bucket_memo):
        matched_non_zero = False
        student_number = 0
        digit = 0

        while True:
            digit_offset = 1 if digit == 0 else 0
            p = 0 if num_students == 0 else int(math.log10(num_students))

            # Not last digit, so do complex magic
            if p > 0 and not matched_non_zero:
                e = pow(10, p)
                d, r = divmod(num_students, e)
                next_digit, accum_index = self.find_digit(index, digit_offset, e, d, r, bucket_memo)

                # Add digit to student number
                student_number *= 10
                student_number += next_digit

                # Adjust index, +1 is for digits with less characters than maximally possible (i.e. 1 instead of 10)
                if index == accum_index: break
                index -= accum_index + 1
                digit += 1

                # Next digit is based on digit chosen
                if next_digit < d:
                    num_students = pow(10, p) - 1
                elif next_digit > d:
                    num_students = pow(10, p - 1) - 1
                else:
                    digit_offset = 1 if digit == 0 else 0
                    next_num_students = num_students % pow(10, p)

                    # Adjust for zeroes not at last digit (i.e. 105)
                    while next_num_students < pow(10, p - 1) or p == 0:
                        p -= 1
                        if not matched_non_zero:
                            e = pow(10, p)
                            d, r = divmod(num_students, e)
                            carry_zeroes = r + self.bucket_base(e // 10, bucket_memo) + 1
                            next_digit, accum_index = self.find_digit_zeroes(index, num_students, digit_offset, e, carry_zeroes, bucket_memo)

                            if next_digit > 0:
                                matched_non_zero = True

                            # Add digits to student number
                            student_number *= 10
                            student_number += next_digit

                            # Adjust inde
                            if index == accum_index: break
                            index -= accum_index + 1
                            digit += 1
                            if matched_non_zero:
                                num_students = pow(10, p - 1)
                            else:
                                num_students = pow(10, p) + r
                        else:
                            next_digit, accum_index = self.find_digit_single(index, digit_offset, bucket_memo, pow(10, p - 1))

                            # Add digits to student number
                            student_number *= 10
                            student_number += next_digit

                            # Adjust index
                            if index == accum_index: break
                            index -= accum_index + 1
                            num_students = pow(10, p)
                    else:
                        num_students = next_num_students
                        continue
                    break

            # Last digit requires special care
            else:
                next_digit, accum_index = self.find_digit_single(index, digit_offset, bucket_memo, 1 if p == 0 else pow(10, p - 1))

                student_number *= 10
                student_number += next_digit

                # Adjust index
                if index == accum_index: break
                index -= accum_index + 1
                if p == 0: break
                num_students = pow(10, p - 1)

        return student_number

    def solve(self, A, B):
        bucket_memo = {}
        return [self.find_student(i - 1, A, bucket_memo) for i in B]
