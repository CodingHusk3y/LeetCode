import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def sieve(n: int) -> list:
            """ Return a list of primes up to n (inclusive) using the Sieve of Eratosthenes. """
            is_prime = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            return [p for p in range(2, n + 1) if is_prime[p]]
        
        def count_special_numbers(l: int, r: int) -> set:
            """ Return a set of special numbers (squares of primes) within range [l, r]. """
            max_check = int(math.sqrt(r)) + 1
            primes = sieve(max_check)
            special_numbers = set()
            for p in primes:
                p_squared = p * p
                if l <= p_squared <= r:
                    special_numbers.add(p_squared)
            return special_numbers
        
        special_numbers = count_special_numbers(l, r)
        total_numbers = r - l + 1
        special_count = len(special_numbers)
        
        return total_numbers - special_count


