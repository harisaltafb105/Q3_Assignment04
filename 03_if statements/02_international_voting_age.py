P_voting_age= int(16)
R_voting_age= int(25)
Y_voting_age= int(45)
def main():
    age=input("HOW OLD ARE YOU: ")
    age = int(age)
    if age >= P_voting_age and age < R_voting_age:
        print("You are eligible to vote in P country")
    elif age >= R_voting_age and age < Y_voting_age:
        print("You are eligible to vote in R country")
    elif age >= Y_voting_age:
        print("You are eligible to vote in Y country")
    
main()