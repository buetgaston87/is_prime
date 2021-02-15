#!/bin/python3
from primes import is_prime

def main():    
    dct = {True: "prime", False: "composite"}
    print("Input a natural number grater than 1 to know if it is prime, 0 (zero) or 1 (one) to exit.")
    num = int(input("Number: "))
    while num > 1:
        print(str(num)+" is a "+dct[is_prime(num)]+" number.")
        num = int(input("Number: "))

if __name__ == "__main__":
    main()