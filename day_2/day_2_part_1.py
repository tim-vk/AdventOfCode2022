def symbol_to_score(symbol):
    if symbol == "X":
        return 1
    if symbol == "Y":
        return 2
    if symbol == "Z":
        return 3


def match(opponent, me):
    score = 0

    # draw
    if (opponent == "A" and me == "X") \
            or (opponent == "B" and me == "Y") \
            or (opponent == "C" and me == "Z"):
        score = 3
    # win
    elif (opponent == "A" and me == "Y") \
            or (opponent == "B" and me == "Z") \
            or (opponent == "C" and me == "X"):
        score = 6
    # lose
    else:
        score = 0

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
