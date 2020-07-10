import random

print("მოგესალმებათ შემთხვევითი რიცხვის გენერატორი!")

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

while num1 == 0 and num2 == 0:
    print("აუცილებელია, რომ მეორე ციფრი იყოს მეტი 0-ზე! ")
    try:
        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    except:
        print("...")
    break

while num1 > num2:
    print("აუცილებელია, რომ პირველი რიცხვი იყოს ნაკლები მეორეზე!")
    try:

        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    except:
        print("...")

if num1 < num2:
    print("თქვენი შემთხვევითი რიცხვი არის -", (random.randrange(num1, num2)))
