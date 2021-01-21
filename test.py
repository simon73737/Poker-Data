# This file used to test things we can do with the file
import csv

player_name = "PATRICK"
files = ["12.29", "1.1", "1.2", "1.3", "1.4", "1.7", "1.14"]
log = []
hand = []
hand_history = []
hands_won = 0
amount_won = 0
num_hands = 0
buy_backs = 0
total_buy_in = 0
total_stack = 0
net_earnings = 0

for name in files:
    file_name = 'Poker_Logs_' + name + '.txt'
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            token = row[0]
            length = len(token)
            idx = 0
            while idx < length:
                if token[idx] == '@':
                    token = token[:idx - 1] + token[idx + 12:]
                    length = len(token)
                idx += 1
            log.insert(0,token)

            buy_in = ""
            if token.find('participation') != -1 and token.find(player_name) != -1:
                buy_backs += 1
                idx = token.find('of ') + 3
                while token[idx] != '.' and len(buy_in) <= 3:
                    buy_in += token[idx]
                    idx += 1
                total_buy_in += int(buy_in)
        
    # Our list (log) is now filled with one file's worth of hands

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


    value = ""
    print_hand = True
    #print("Printing hands from: " + file_name + " in which " + player_name + " won more than 1000")
    for hand in hand_history:
        for row in hand:
            if row.find("Omaha") != -1 and print_hand:
                print_hand = False
            if row.find("Texas") != -1:
                print_hand = True
            # Check to see if the row in the hand tells us who won the hand
            if row.find(player_name) != -1 and row.find("collected") != -1:
                hands_won += 1
                idx = row.find("collected") + 10
                while row[idx] != ' ':
                    value += row[idx]
                    idx += 1
                amount_won += int(value)

                #if int(value) >= 500 and print_hand:
                    #for line in hand:
                        #print(line)
                    #print("-----------------------------------------------------------------------------------------------------------------------------------")
                value = ""
    
            if row.find('Player stacks:') != -1 and row.find(player_name) != -1:
                stack = ""
                idx = row.find(player_name) + 3 + len(player_name)
                while row[idx] != ')':
                    stack += row[idx]
                    idx += 1
                total_stack = int(stack)
                stack = ""
    net_earnings += total_stack

    print
    print
    log = []
    hand_history = []

print("Printing data for " + player_name)
print(player_name + " won: " + str(hands_won) + " hands.")
if hands_won != 0:
    print(player_name + " won: " + str(amount_won * 1.0 / hands_won) + " on average per hand they won.")
print("Number of buy ins for " + player_name + ": " + str(buy_backs))
print(player_name + " bought in for a total of: " + str(total_buy_in))
print(player_name + "'s net earnings is: " + str(net_earnings - total_buy_in))

                    