def fruit():
    fruit_prices = {
        "apple": 3.2,
        "banana": 1.5,
        "pear": 2.5,
        "orange": 7.8,
        "grape": 12.0,
        "kiwi": 15.5
    }
    fruit1 = int(input("How many apples do you want? "))
    fruit2 = int(input("How many bananas do you want? "))
    fruit3 = int(input("How many pears do you want? "))
    fruit4 = int(input("How many oranges do you want? "))
    fruit5 = int(input("How many grapes do you want? "))
    fruit6 = int(input("How many kiwis do you want? "))

    total = (fruit_prices["apple"] * fruit1) + (fruit_prices["banana"] * fruit2) + \
            (fruit_prices["pear"] * fruit3) + (fruit_prices["orange"] * fruit4) + \
            (fruit_prices["grape"] * fruit5) + (fruit_prices["kiwi"] * fruit6)
    print("The total is: " + str(total))
    return total


print(fruit())

