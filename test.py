#Johnathan Sullivan

#This Program counts to 100 entered by the number chosen by the user

#print("Let's Count to 100")
#num_count = int(input("What number do you wish to count by? "))
#for number in range (num_count, 101,num_count):
    #if num_count <  101 - 1:
        #print(number, end=',')
#else:
    #print (number)

#I could have tried to use a "Loop-hole" in the directions and just print the final number is _ so it would /
# always print "Final number _ " thus not ending with a comma. I didn't want to lose points to just be an arsehole.

#Johnathan Sullivan

#This Program counts to 100 entered by the number chosen by the user

print("Let's Count to 100")
num_count = int(input("What number do you wish to count by? "))
for number in range (num_count, 101,num_count):
    if num_count <  101 - 1 and num_count <= 100 - 1:
        print(number, end=',')
else:
    print(f'final number', number, end='')


