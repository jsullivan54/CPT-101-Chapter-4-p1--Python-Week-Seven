#Johnathan Sullivan

#This program uses a loop to print the lyrics for "Five Little Monkeys Jumping on the Bed."

#However, change it, so that the user can enter the number of monkeys to start with.

#Use a for loop to start at the number input by the uses and work backwards through "no more monkeys jumping on the bed."

#You MUST use a for loop and a variable in your print statements.



#User will enter the number of monkeys below
num_monkeys = int(input('How may monkeys are jumping on the bed? : '))
for monkeys in range (num_monkeys, 0, -1):
        print(f'{monkeys} One fell off and bumped their head,mama called the Dr., '
              f'and the Dr. said,no more monkeys jumping on the bed')


