# This file used to test things we can do with the file
import csv

player_name = "AJ"

date_of_log = 1.7
log = []
hand = []
hand_history = []
file_name = 'Poker_Logs_' + str(date_of_log) + '.txt'
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    flop_count = 0
    paired_flop_count = 0
    stack = ""
    total_stack = 0
    num_hands = 0

    # Loop through each line of the file
    # We only care about row[0]
    for row in csv_reader:
        token = row[0]
        # Here were going to clean up each token by removing the _@xxxxxxxxxx after each player name
        length = len(token)
        idx = 0
        while idx < length:
            if token[idx] == '@':
                token = token[:idx - 1] + token[idx + 12:]
                length = len(token)
            idx += 1
        log.insert(0, token)

add = False
for row in log:
    if row.find("starting") != -1:
        add = True
    elif row.find("ending") != -1:
        add = False
        hand.append(row)
        hand_history.append(hand)
        hand = []
    if add:
        hand.append(row)

hands_won = 0
amount_won = 0
value = ""
for element in hand_history:
    for token in element:
        if token.find(player_name) != -1 and token.find("collected") != -1:
            print("Printing all hands won by: " + player_name)
            for line in element:
                print(line)
            print("--------------- NEXT HAND ------------------")
            hands_won += 1
            idx = token.find("collected") + 10
            while token[idx] != ' ':
                value += token[idx]
                idx += 1
            amount_won += int(value)
            value = ""

print(player_name + " won: " + str(hands_won) + " hands.")
if hands_won != 0:
    print(player_name + " won: " + str(amount_won * 1.0 / hands_won) + " on average per hand they won.")


# Print out all of the data that weve found
#print("Average stack for " + player_name + ": " + str(total_stack * 1.0 / num_hands))
                    