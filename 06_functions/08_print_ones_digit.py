def ones_digit(n):
    """
    This function takes an integer n and returns the ones digit of n.
    """
    return n % 10   

def main():
    """
    This function prompts the user for an integer and prints the ones digit of that integer.
    """
    n = int(input("Enter an integer: "))
    print(f"The ones digit of {n} is {ones_digit(n)}")

if __name__ == '__main__':  
    main()