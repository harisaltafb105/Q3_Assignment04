def evennum():
    
    even_numbers = []
    while even_numbers == []:
        even_num= int(input("Enter a number: "))
        even_numbers.append(even_num)
    return even_numbers
        
    


def main(even_numbers):
    for i in even_numbers:
        if i % 2 == 0:
            print(f"{i} is an even number")
        else:
            print(f"{i} is not an even number")

main(evennum())
