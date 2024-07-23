n = int(input("Please enter the number: "))
is_prime = True

if n < 2:
     print(f"{n} is not a prime number")

else:
    # We check for divisibility upto the square root of the number. If a number is divisble by a number less or equal to its square root, then it has to be divisible a number larger than it's square root.
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            is_prime = False
            print(f'{n} is not a prime number')
            break

    else:
        print(f'{n} is a prime number')




