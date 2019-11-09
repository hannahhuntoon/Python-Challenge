import csv
import os


csvpath = os.path.join("election_data.csv")

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
   
votes = 0; uniqueCandidates = []; candidatesVotes = [] 

with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        votes = votes + 1
        candidate = (row[2])
        if candidate in uniqueCandidates:
            candidateIndex = uniqueCandidates.index(candidate)
            candidatesVotes[candidateIndex] = candidatesVotes[candidateIndex] + 1
        else:
            uniqueCandidates.append(candidate)
            candidatesVotes.append(1)


percentages = []; maxVotes = candidatesVotes[0]; maxIndex = 0

for count in range(len(uniqueCandidates)):
    percentVotes = candidatesVotes[count]/votes*100
    percentages.append(percentVotes)
    if candidatesVotes[count] > maxVotes:
        maxVotes = candidatesVotes[count]
        print(maxVotes)
        maxIndex = count 
winner = uniqueCandidates[maxIndex]

percentages = [round(i,2) for i in percentages]

print(f'ELection Results')
print(f'Total Votes {votes}')
for count in range(len(uniqueCandidates)):
    print(f'{uniqueCandidates[count]}: {percentages[count]}% ({candidatesVotes[count]})')
print(f'Winner: {winner}')

with open ("poll.txt", "w") as output:
        line = (f'The Election Results are as follows: There were {votes} Total Votes  and the winner is {winner} with 63% of votes.')
        output.write(line)        
