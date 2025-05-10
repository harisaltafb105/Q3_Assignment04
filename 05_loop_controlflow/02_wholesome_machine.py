words= "I am capable of doing any thing"
def get_words():
    your_words = input("Enter your words: ")
    while your_words != words:
        print("You are not capable of doing any thing")
        your_words = input("Enter your words: ")


get_words()
print("you ar right you are capable of doing any thing")