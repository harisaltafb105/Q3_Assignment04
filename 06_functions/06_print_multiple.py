def print_multiple(message, repeat):
    """Prints a message multiple times."""
    for _ in range(repeat):
        print(message)

def main():
    message = input("Enter a message: ")
    repeat = int(input("How many times do you want to print it? "))
    print_multiple(message, repeat)

if __name__ == '__main__':
    main()