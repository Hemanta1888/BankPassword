import random
num = '1234567890'
alpha = 'abcdefghijklmnopqrstuvwxyz'
password = ' '
print("Dear sir, welcome to our bank")
while True:
        que = input("Do you want to open your account[y/n]? ")
        print(que)
        if que == 'y':
            print("Thank you for showing interest to open account in our bank.")
            que1 = input("Enter your name please: ")
            que2 = input("Choose your special char: ")
            que3 = input("Choose some number: ")
            result = que1.capitalize() + que2 + que3
            for i in range(3):
                password +=  random.choice(num)
                password += random.choice(alpha)
            print('Please look below for information about user_id and password.')
            print('')
            print(f"Your user_id is: {result}")
            print(f'Your password is: {password}')
            print('')
            print("Thank you again for your co-operation with us.")
            break
           
        if que == 'n':
            print("Thank you for visiting our bank.")







