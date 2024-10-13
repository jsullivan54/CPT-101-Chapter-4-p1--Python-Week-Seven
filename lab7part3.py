#Johnathan Sullivan

#This Program counts to 100 entered by the number chosen by the user

print("Let's Count to 100")
num_count = int(input("What number do you wish to count by? "))
for number in range (num_count, 101,num_count):
    if number < 101 - 1 and number < 96:
        print(number, end=',')
else:
    print(number, end='')




