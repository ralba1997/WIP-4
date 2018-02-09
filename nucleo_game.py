print('\nDescription'
      '\n We have 4 nucleotides randomly ordered in an unknown length of a sequence.'
      '\n There are two players competing to win, such that if one is left with '
      '\na single or a one type nucleotide of any number, one will lose the game')
def game(Nucleotide_Sequence):
    a = 0
    t = 0
    c = 0
    g = 0

    for i in Nucleotide_Sequence:
        if i == 'A':
            a += 1
        elif i == 'T':
            t += 1
        elif i == 'C':
            c += 1
        elif i == 'G':
            g += 1

    total = sum(Nucleotide_Sequence)
    values = []
    if a != 0:
        values.append(a)
    if t != 0:
        values.append(t)
    if c != 0:
        values.append(c)
    if g != 0:
        values.append(g)
    # Case1

    if total <= 2:
        print("Impossible game")

    # Case2
    if total % 3 == 0:
        print("Second will win anyway")
        # Since the second player takes one if the first took 2 and vice versa!
    if total % 3 == 1:
        minvalue = min(values)
        if a == minvalue:
            a -= 1
        if t == minvalue:
            t -= 1
        if c == minvalue:
            c -= 1
        if g == minvalue:
            g -= 1

    # Case3
    if total % 3 == 2:
        if a and (t + c + g) == 4:
            a -= 1
            t -= 1
        if t and (a + c + g) == 4:
            t -= 1
            c -= 1
        if c and (a + c + g) == 4:
            c -= 1
            g -= 1
        if g and (a + t + c) == 4:
            g -= 1
            a -= 1
        maxvalue = max(values)
        if a == maxvalue:
            a -= 2
        if t == maxvalue:
            t -= 2
        if c == maxvalue:
            c -= 2
        if g == maxvalue:
            g -= 2
    return (a, t, c, g)


def nucleo_game(a, t, c, g): #HERE I HAVE USED A RECURSIVE FUNCTION TO CALL THE MAIN FUNCTION UNTIL GAME FINISHES
    if a + t + c or a + t + g or t + c + g == 0:
        condition = True
        print('You won the game')
    else:
        condition = False
    while condition == False:
        game(nucleo_game())
nucleo_game(6,27,3,45)