def is_prime(num):
    isPrime = True

#Error #1 - generate numbers from 2 through num - 1
    for i in range(2, num -1):
#Error #2 - double equal sign
        if num % i == 0:
            isPrime = False

    return isPrime

def main():
#Error #3 - end loop header with colon
    for i in range(1, 101):
#Error #4 - change isPrime to is_prime
        if is_prime(i) == True:
            print(i, "is a prime number")

#Error #5 - improper indentation
main()