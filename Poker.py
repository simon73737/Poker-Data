#Importing packages we need
import csv
# List of all files we want to get data from
files = ["12.29", "1.1", "1.2", "1.3", "1.4", "1.7"]
# Variables which keep track of total data, not data by file
val = ""
flop_count = 0
paired_flop_count = 0
player_name = "SIMON"
num_hands = 0
stack = ""
total_stack = 0

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
            
            # Look at all tokens which give us the flop of a hand
            if token[0] == 'F':
                index = 8
                # Look at the first card on the flop
                c1 = token[index]
                if c1 == '1':
                    index += 1
                    c1 += token[index]
                index += 6
                # Look at the second card on the flop
                c2 = token[index]
                if c2 == '1':
                    index += 1
                    c2 += token[index]
                index += 6
                # Look at the third card on the flop
                c3 = token[index]
                if c3 == '1':
                    index += 1
                    c3 += token[index]
                # Check to see if we have a paired flop
                if c1 == c2 or c1 == c3 or c2 == c3:
                    paired_flop_count += 1
                flop_count += 1

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

print("Printing data about the flops:")
print("Number of flops: " + str(flop_count))
print("Number of paired flops: " + str(paired_flop_count))
print("This equates to: " + str((paired_flop_count * 100.0) / flop_count) + "% of flops being paired.")
print("Normally we would expect about 17% of flops to be paired.")
print("------------------------------------------------------")
print("Average stack for " + player_name + ": " + str(total_stack * 1.0 / num_hands))