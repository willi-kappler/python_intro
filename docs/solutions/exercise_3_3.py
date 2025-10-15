import random

def get_price(age):
    price = 0

    if age < 5:
        price = 0
    elif age >= 5 and age < 12:
        price = 5
    elif age >= 12 and age < 18:
        price = 10
    elif age >= 18:
        price = 15

    return price

age = int(input("What age are you? "))
print(f"You have to pay: {get_price(age)}")

ages = random.sample(range(0, 99), 20)
prices = []

for age in ages:
    prices.append(get_price(age))

print(f"The ages are: {ages}")
print(f"The prices are: {prices}")
print(f"The total price is: {sum(prices)}")
