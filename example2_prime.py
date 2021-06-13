#!/bin/python3
from primes import primes_number_generator

def main():        
    print("Input an integer number grater than 1 to know all the prime numbers from 2 to the given number. Ctrl+c to exit.")
    try:
        while True:    
            try:
                num = int(input("Number: "))
                print("List of primes numbers: ", primes_number_generator(num))
            except AssertionError as e:
                print(e)
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        print("\nThe end!!")

if __name__ == "__main__":
    main()
