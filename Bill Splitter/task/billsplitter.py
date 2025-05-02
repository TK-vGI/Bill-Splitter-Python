# Stage 3
# [5, [Marc, Jem, Monica, Anna, Jason], 100, Yes]
import random


print('Enter the number of friends joining (including you):')
party_number = int(input())
party = {}
if party_number > 0:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(party_number):
        party[input()] = 0

    print("\nEnter the total bill value:")
    final_bill = float(input())
    split = round(final_bill / party_number, 2)

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_choice = input()
    if lucky_choice == 'Yes':
        random_person = random.choice(list(party.keys()))
        print(f'{random_person} is the lucky one!')
    else:
        print('\nNo one is going to be lucky')

else:
    print('\nNo one is joining for the party')

# End of Stage 3


# # Stage 2
# print('Enter the number of friends joining (including you):')
# party_number = int(input())
# party = {}
# if party_number > 0:
#     print('\nEnter the name of every friend (including you), each on a new line:')
#     for _ in range(party_number):
#         party[input()] = 0
#
#
#     final_bill = float(input("\nEnter the total bill value: "))
#     split = round(final_bill / party_number, 2)
#
#     for name in party:
#         party[name] = split
#
#     print()
#     print(party)
#
# else:
#     print('\nNo one is joining for the party')
#
# # End of Stage 2


# # Stage 1
# def party_create():
#     print('Enter the number of friends joining (including you):')
#     party_number = int(input())
#     party = {}
#     if party_number > 0:
#         print ('Enter the name of every friend (including you), each on a new line:')
#         for _ in range(party_number):
#             party[input()] = 0
#
#         return party
#     else:
#         return 'No one is joining for the party'
#
#
# print(party_create())
#
# End of Stage 1