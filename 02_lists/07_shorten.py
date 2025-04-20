MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print(removed)

def main():
    sample_list = input("Enter list items separated by spaces: ").split()
    shorten(sample_list)

main()
