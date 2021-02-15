#!/bin/python3

# Return True if a given natural number is prime and False if it is not
def is_prime(num):
    if num < 2:
        return False    
    for n in range(2,num):
        if num%n == 0:
            return False
        if num%n > 1:
            return True
    return True

# Return a list of all the prime numbers from 2 to the given number. The input must be a natural number
def primes_number_generator(num):
    primes = []
    for n in range(num):
        if is_prime(n):
            primes.append(n)
    return primes