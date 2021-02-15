#!/bin/python3
from primes import primes_number_generator

def main():        
    print("Input a natural number grater than 1 to know all the prime numbers from 2 to the given number, 0 (zero) or 1 (one) to exit.")
    num = int(input("Number: "))
    while num > 1:
        print("List of primes numbers: ", end="")
        print(primes_number_generator(num))
        num = int(input("Number: "))

if __name__ == "__main__":
    main()