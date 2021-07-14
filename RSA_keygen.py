# This is a sample Python script.

import random


class RSAkeygen:
    low_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    MAX_32_BIT = 4294967295

    def generate_key(self):
        p = self.generate_prime()
        q = self.generate_prime()
        while p == q:
            q = self.generate_prime()

        print(p, q)

        n = p * q
        l = self.least_common_multiple(p - 1, q - 1)

        e = self.generate_prime(maximum = l - 1)
        while l % e == 0:
            e = self.generate_prime(maximum = l - 1)

        d = pow(e, -1, l)

        return [n, e, d]

    def least_common_multiple(self, number1, number2):
        retval = (number1*number2) / self.greatest_common_divisor(number1, number2)
        return int(retval)

    @staticmethod
    def greatest_common_divisor(number1, number2):
        arr = [number1, number2]
        while arr[0] != 0 or arr[1] != 0:
            arr = [arr[0], arr[1] % arr[0]]
            if arr[0] == 0 or arr[1] == 0:
                break
            arr = [arr[1], arr[0] % arr[1]]

        if arr[0] != 0:
            return arr[0]
        else:
            return arr[1]

    def generate_low_level_prime(self, maximum=-1):
        finished = False

        while not finished:
            finished = True

            # generate odd random 16-bit number
            number = 0
            if maximum == -1:
                while (number < 32768) or (number % 2 == 0):
                    number = random.getrandbits(16)
            else:
                while (number % 2 == 0):
                    number = random.randint(1, maximum)

            # check low-prime divisibility
            for low_prime in self.low_primes:
                if number % low_prime == 0:
                    finished = False
                    break

        return number

    @staticmethod
    def perform_rabin_miller_test(number, repeats=20):

        factor = number - 1
        exponent = 0

        # factorisation -> number = factor**exponent + 1
        while factor % 2 == 0:
            factor /= 2
            exponent += 1

        for i in range(repeats):
            continue_main_loop = False

            a = random.randint(2, number - 2)
            x = pow(a, int(factor), number)

            if x == 1 or x == number - 1:
                continue

            for j in range(exponent - 1):
                x = pow(x, 2, number)
                if x == number - 1:
                    continue_main_loop = True
                    break

            if not continue_main_loop:
                return False

        return True

    def generate_prime(self, maximum=-1):

        finished = False

        while not finished:
            finished = True

            # generate low-level prime
            number = self.generate_low_level_prime(maximum)

            for i in range(20):
                if self.perform_rabin_miller_test(number) == False:
                    finished = False
                    break

        return number
