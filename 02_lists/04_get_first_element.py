def get_first_element(lst):
    print(lst[0])

def main():
    items = []
    while True:
        val = input("Enter a list item (or press enter to finish): ")
        if val == "":
            break
        items.append(val)
    get_first_element(items)

main()
