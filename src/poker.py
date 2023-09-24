
hands = ["High Card", "Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

file_path = input()

file = open(file_path, "r+")

number_of_hands = int(file.readline())


def print_result(result):
    print(hands[result - 1])
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


def el():
    all_cards = file.readlines()
    for i in range(len(number_of_hands)):
        cards_in_round = all_cards[i+1].split(sep=" ")
        return cards_in_round



def calculate_result(cards_in_round):
    dict_round = {
        1 : cards_in_round[0].split(),
        2 : cards_in_round[1].split(),
        3 : cards_in_round[2].split(),
        4 : cards_in_round[3].split(),
        5 : cards_in_round[4].split()
    }

    for i in range(len(dict_round.keys())):
        for j in range(2):
            if dict_round[i][j]=="T":
                dict_round[i][j] = 10
            if dict_round[i][j]=="J":
                dict_round[i][j] = 11
            if dict_round[i][j]=="Q":
                    dict_round[i][j] = 12
            if dict_round[i][j]=="K":
                dict_round[i][j] = 13
            if dict_round[i][j]=="A":
                    dict_round[i][j] = 14
            else:
                dict_round[i][j] = int(dict_round[i][j])

    list_of_values= [dict_round[1][1],dict_round[2][1],dict_round[3][1],dict_round[4][1],dict_round[5][1]]
    list_of_suits = [dict_round[1][2],dict_round[2][2],dict_round[3][2],dict_round[4][2],dict_round[5][2]]

    list_of_values1 = list_of_values.sort()
    if ([dict_round[1][2],dict_round[2][2],dict_round[3][2],dict_round[4][2],dict_round[5][2]] == ["H", "H", "H", "H", "H"] or [dict_round[1][2],dict_round[2][2],dict_round[3][2],dict_round[4][2],dict_round[5][2]] == ["D", "D", "D", "D", "D"] or [dict_round[1][2],dict_round[2][2],dict_round[3][2],dict_round[4][2],dict_round[5][2]] == ["C", "C", "C", "C", "C"] or [dict_round[1][2],dict_round[2][2],dict_round[3][2],dict_round[4][2],dict_round[5][2]] == ["S", "S", "S", "S", "S"]) and list_of_values1 == [10,11,12,13,14]:
        print(hands[9])




cards= el()
print(cards)
for i in range(number_of_hands):
    print(calculate_result(cards)

file.close()

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

