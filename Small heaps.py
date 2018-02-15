import random
global specialtriplets
global winning_moves
specialtriplets = []
winning_moves={}

# Special triplets are built and appended to the list
def find_specialtriplets():
    triplets=[]
    aspecialtriplets=[]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                triplet=[i,j,k]
                append_to_list(triplet,specialtriplets)
    return specialtriplets

# A triplet is added to the list if it is not already present
def append_to_list(atriplet,alist):
    if sorted(atriplet) not in alist:
        alist.append(sorted(atriplet))


# Returns the list of the triplets in which only one number is reduced by 1
def find_triplets_m1(atriplet):
    i=atriplet[0]
    j=atriplet[1]
    k=atriplet[2]
    atripletsm1=[]
    if i >= 1:
        append_to_list([i - 1, j, k],atripletsm1)
    if j >= 1:
        append_to_list([i, j - 1, k], atripletsm1)
    if k >= 1:
        append_to_list([i, j, k - 1], atripletsm1)
    return atripletsm1

# Returns the list of the triplets in which the sum is reduced by 2 (taking two elements from one of the numbers
# or one element from two numbers)
def find_triplets_m2(atriplet):
    i=atriplet[0]
    j=atriplet[1]
    k=atriplet[2]
    atripletsm2=[]
    if i >= 2:
        append_to_list([i - 2, j, k], atripletsm2)
    if j >= 2:
        append_to_list([i , j - 2, k], atripletsm2)
    if k >= 2:
        append_to_list([i , j, k - 2], atripletsm2)
    if i >= 1 and j >= 1:
        append_to_list([i - 1, j - 1, k], atripletsm2)
    if i >= 1 and k >= 1:
        append_to_list([i - 1, j, k - 1], atripletsm2)
    if j >= 1 and k >= 1:
        append_to_list([i, j - 1, k - 1], atripletsm2)
    return atripletsm2

# Looks for a losing position on the same row which is 1 column on the left or 2 columns on the left
# If found, the position is put inside the dictionary and it is the next move to do
def searchinsamerow(aspecialtriplet,l):
    found0 = False
    if l >= 1:
        if winning_moves[tuple(aspecialtriplet)][l - 1] and winning_moves[tuple(aspecialtriplet)][l - 1] == 1:
            winning_moves[tuple(aspecialtriplet)][l] = [aspecialtriplet, -1]
            found0 = True
    if l >= 2:
        if winning_moves[tuple(aspecialtriplet)][l - 2] and winning_moves[tuple(aspecialtriplet)][l - 2] == 1:
            winning_moves[tuple(aspecialtriplet)][l] = [aspecialtriplet, -2]
            found0 = True
    return found0


# Looks for a losing position in the values corresponding to the triplets whose sum is 2 less than the sum of the triplet
# It can be found only in the same column
# If found, the position is put inside the dictionary and it is the next move to do
def searchintriplets_m2(aspecialtriplet,l):
    triplets_m2 = find_triplets_m2(aspecialtriplet)
    found2 = False
    for triplet in triplets_m2:
        if winning_moves[tuple(triplet)][l] and winning_moves[tuple(triplet)][l] == 1:
            winning_moves[tuple(aspecialtriplet)][l] = [triplet,0]
            found2 = True
    return found2

# Looks for a losing position in the values corresponding to the triplets whose sum is 1 less than the sum of the triplet
# It can be found in the same column or in the previous column
# If found, the position is put inside the dictionary and it is the next move to do
def searchintriplets_m1(aspecialtriplet,l):
    found1 = False
    triplets_m1 = find_triplets_m1(aspecialtriplet)
    for triplet in triplets_m1:
        if winning_moves[tuple(triplet)][l] and winning_moves[tuple(triplet)][l] == 1:
            winning_moves[tuple(aspecialtriplet)][l] = [triplet, 0]
            found1 = True
        if winning_moves[tuple(triplet)][l - 1] and winning_moves[tuple(triplet)][l - 1] == 1:
            winning_moves[tuple(aspecialtriplet)][l] = [triplet, -1]
            found1 = True
    return found1

# Fills the dictionary in which the keys are the triplets and the values are lists
# with l elements (l corresponds to the fourth element of the sequence reduced by 1)
# The l-element of the list is 1 if the position is losing, whereas it is the nearest
# losing position and the next move to do)
def fill_winning_moves(sequence):
    winning_moves[tuple([0, 0, 0])] = [1, 1, 1, 1, 1, 1] # The position [0, 0, 0, n] is losing for any n
    specialtriplets.remove([0, 0, 0])

    n = sequence[3]
    l = n-1
    for specialtriplet in specialtriplets: # Special triplets are analyzed one by one
        winning_moves[tuple(specialtriplet)] = [None for i in range(6)] # At the beginning the list is all None
        for l in range(6):
            if l+1 >= specialtriplet[2]: # This is useful only for n >= last number in the triplet (the sequence is sorted)
                found = False
                found = searchinsamerow(specialtriplet, l)
                if not found:
                    found = searchintriplets_m2(specialtriplet, l)
                if not found:
                    found = searchintriplets_m1(specialtriplet, l)
                if not found:
                    winning_moves[tuple(specialtriplet)][l] = 1 # It is set to 1 if the position is losing

# If the position is a losing one, a random move is done
def random_move(atriplet, an):
    random_n = random.randint(1,2)
    if random_n == 2 and an >= 2:
        anewseq = atriplet + [an - random_n]
    else:
        anewseq = atriplet + [an - 1]
    return anewseq


specialtriplets = find_specialtriplets()



na=int(input("nA? "))
nc=int(input("nC? "))
ng=int(input("nG? "))
nt=int(input("nT? "))
sequence = [na, nc, ng, nt]
print("starting sequence: ", sequence)
fill_winning_moves(sequence)


j = 0
mods = sum(sequence) % 3
ordseq = sorted(sequence)
while not (ordseq[0] == 0 and ordseq[1] == 0 and ordseq[2] == 0): # Until the game does not end, moves are done
    j += 1
    triplet = ordseq[:3]
    n = ordseq[3]
    modn = n % 3
    modt = sum(triplet)%3
    if triplet in specialtriplets:
        if modn == 0:  # If modn == 0, the move is the same as n == 6, i.e. l = 5
            if winning_moves[tuple(triplet)][5] == 1:
                newseq = random_move(triplet, n)
            else:
                newtriplet = winning_moves[tuple(triplet)][5][0]
                newn = n + winning_moves[tuple(triplet)][5][1]
                newseq = newtriplet+[newn]
        if modn == 1:  # If modn == 1, the move is the same as n == 4, i.e. l = 3
            if winning_moves[tuple(triplet)][3] == 1:
                newseq = random_move(triplet, n)
            else:
                newtriplet = winning_moves[tuple(triplet)][3][0]
                newn = n + winning_moves[tuple(triplet)][3][1]
                newseq = newtriplet+[newn]
        if modn == 2:  # If modn == 2, the move is the same as n == 5, i.e. l = 4
            if winning_moves[tuple(triplet)][4] == 1:
                newseq = random_move(triplet, n)
            else:
                newtriplet = winning_moves[tuple(triplet)][4][0]
                newn = n + winning_moves[tuple(triplet)][4][1]
                newseq = newtriplet+[newn]
    else:
        if mods == 0:
            newseq = random_move(triplet, n)
        elif mods == 1:
            newseq = triplet + [n - 1]
        elif mods == 2:
            newseq = triplet + [n-2]

    ordseq = sorted(newseq)
    print(j % 2, ordseq)

