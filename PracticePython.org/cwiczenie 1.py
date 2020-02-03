name = input("Please enter Your Name: ")
age = input("Please enter Your Age: ")

new_age = 100 - int(age)
multi = int(input("how many times You want the message to appear?"))

for i in range(multi):
    print('You will be 100 years old in: ' + str(new_age) + ' years')
              

