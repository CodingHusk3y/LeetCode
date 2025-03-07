class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False

        for num in range(2, int(right ** 0.5) + 1):
            if primes[num]:
                for multiple in range(num * num, right + 1, num):
                    primes[multiple] = False

        prime_list = [i for i in range(left, right + 1) if primes[i]]

        if len(prime_list) < 2:
            return [-1, -1]

        min_diff = float('inf')
        closest = []

        for i in range(1, len(prime_list)):
            diff = prime_list[i] - prime_list[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest = [prime_list[i - 1], prime_list[i]]

        return closest
