#!/bin/python3
from primes import is_prime

def main():    
    dct = {True: "prime", False: "composite"}
    print("Input an integer number grater than 1 to know if it is prime. Ctrl+c to exit.")
    try:
        while True:    
            try:
                num = int(input("Number: "))
                print(str(num)+" is a "+dct[is_prime(num)]+" number.")                
            except AssertionError as e:
                print(e)
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        print("\nThe end!!")

if __name__ == "__main__":
    main()
