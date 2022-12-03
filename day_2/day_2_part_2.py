def symbol_to_score(symbol):
    if symbol == "A":
        return 1
    if symbol == "B":
        return 2
    if symbol == "C":
        return 3

def match(opponent, me):
    score = 0

    # draw
    if me == "Y":
        score = 3
        me = opponent
    # win
    elif me == "Z":
        score = 6
        if opponent == "A":
            me = "B"
        elif opponent == "B":
            me = "C"
        else:
            me = "A"
    # lose
    else:
        score = 0
        if opponent == "A":
            me = "C"
        elif opponent == "B":
            me = "A"
        else:
            me = "B"

    return score + symbol_to_score(me)

def match_player(filename):
    with open(filename, 'r') as file:
        total_score = 0
        for line in file.readlines():
            play = line.split()
            total_score += match(play[0], play[1])
    return total_score

if __name__ == '__main__':
    result = match_player("input-data")
    print(result)
