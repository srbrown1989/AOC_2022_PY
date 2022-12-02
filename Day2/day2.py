score = 0
normalize = {
    'A': 1,
    'B': 2,
    'C': 3,
    # 'X': 1,
    # 'Y': 2,
    # 'Z': 3,
    'X': 0,
    'Y': 3,
    'Z': 6,
}


# part 1 requires to calculate the outcome of the moves played
def calc_outcome(opponent_move, player_move):
    if opponent_move == player_move:  # draw
        return 3
    if (player_move == 1 and opponent_move) == 3 or \
            (player_move == 2 and opponent_move == 1) or \
            (player_move == 3 and opponent_move == 2):
        return 6
    else:
        return 0


# part 1 : comment out when want part 2.
# with open("data.txt") as file:
#     for line in file:
#         current = line.split()
#         # want to make each move have same value. A & X = 1.
#         opponent = normalize[current[0]]
#         player = normalize[current[1]]
#         # add base score to player
#         score += player
#         score += calc_outcome(opponent, player)
#
# print(score)

# part 2 requires determination of which move to play.
def calc_shape(opponent_move, outcome):
    if outcome == 3:
        return opponent_move
    if outcome == 0:
        if opponent_move == 1:
            return 3
        elif opponent_move == 2:
            return 1
        else:
            return 2
    else:
        if opponent_move == 1:
            return 2
        elif opponent_move == 2:
            return 3
        else:
            return 1

# part 2 : comment out if want part 1.
with open("data.txt") as file:
    for line in file:
        current = line.split()
        opponent = normalize[current[0]]
        match_outcome = normalize[current[1]]
        score += match_outcome # outcome is known so add this score now
        score += calc_shape(opponent, match_outcome)

print(score)

# feels a bit of a clunky solution. will look into ways of getting this cleaner.
