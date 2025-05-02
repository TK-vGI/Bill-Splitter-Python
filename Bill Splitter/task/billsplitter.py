# Stage 1
def party_create():
    print('Enter the number of friends joining (including you):')
    party_number = int(input())
    party = {}
    if party_number > 0:
        print('Enter the name of every friend (including you), each on a new line:')
        for _ in range(party_number):
            party[input()] = 0

        return party
    else:
        return 'No one is joining for the party'


print(party_create())