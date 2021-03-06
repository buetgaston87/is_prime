#!/bin/python3

# Return True if a given number is prime and False if it is not. The input must be a natural number greater than one
def is_prime(num):
    assert type(num) is int, "num is not an integer: %r" % num
    assert num > 1, "num is not greater than one: %r" % num    
    for n in range(2,num):
        if num%n == 0:
            return False
        if num%n > 1:
            return True
    return True

# Return a list of all the prime numbers from 2 to the given number. The input must be a natural number greater than one
def primes_number_generator(num):
    assert type(num) is int, "num is not an integer: %r" % num
    assert num > 1, "num is not greater than one: %r" % num
    return [n for n in range(2,num+1) if is_prime(n)]
