print("Let's Count to 100")
num_count = int(input("What number do you wish to count by? "))
for number in range(num_count, 101, num_count):
    if number < 100:
        print(number, end=', ')
    else:
        print(number, end='')
