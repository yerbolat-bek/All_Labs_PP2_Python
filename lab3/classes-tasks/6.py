class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def get_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_filter = PrimeFilter(numbers)
prime_numbers = prime_filter.get_primes()

print("Простые числа:", prime_numbers)
