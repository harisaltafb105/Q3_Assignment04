def divisor(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
def main():
    n = int(input("Enter a number: "))
    divisors = divisor(n)
    print(f"The divisors of {n} are: {divisors}")

if __name__ == '__main__':
    main()