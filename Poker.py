#Importing packages we need
import csv
# List of all files we want to get data from
files = ["12.29", "1.1", "1.2", "1.3", "1.4", "1.7", "1.14"]
# Variables which keep track of total data, not data by file
player_name = "SIMON"
num_hands = 0
stack = ""
total_stack = 0
buy_backs = 0
total_buy_in = 0

# Loops through and opens and reads from each file
for name in files:
    file_name = 'Poker_Logs_' + name + '.txt'

    buy_back = False

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

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
        
            # Look at all tokens which give us player stacks
            if token[0] == 'P':
                if token.find(player_name) != -1:
                    num_hands += 1
                    idx = token.find(player_name) + 3 + len(player_name)
                    while token[idx] != ')':
                        stack += token[idx]
                        idx += 1
                    total_stack += int(stack)
                    stack = ""

            # Find the number of times the given player has bought in and how much theyve bought in for in total
            buy_in = ""
            if token.find('participation') != -1 and token.find(player_name) != -1:
                buy_backs += 1
                idx = token.find('of ') + 3
                while token[idx] != '.' and len(buy_in) <= 3:
                    buy_in += token[idx]
                    idx += 1
                total_buy_in += int(buy_in)



print("Average stack for " + player_name + ": " + str(total_stack * 1.0 / num_hands))
print("Number of buy ins for " + player_name + ": " + str(buy_backs))
print(player_name + " bought in for a total of: " + str(total_buy_in))