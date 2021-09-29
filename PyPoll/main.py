import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

# initialize variables
TotalVotes = 0
Candidates = []
Votes = []
Election = {"Name": Candidates, "Count": Votes}
Percentage = 0
MostVotes = 0
Winner = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) 
    for row in csvreader:

        # Count total votes in data
        TotalVotes = TotalVotes + 1

        # Tally votes per candidate
        for i in Candidates:
            if row[2] == i:
                j = Candidates.index(i)
                Votes[j] = Votes[j] + 1 

        # Populate lists
        if not row[2] in Candidates:
            Candidates.append(row[2])
            Votes.append(1)

# print results
print("Election Results")
print("------------------------------------------")
print(f"Total Votes: {TotalVotes:,}")
print("------------------------------------------")
MostVotes = Election['Count'][0]
Winner = Election['Name'][0]
for x in range(len(Candidates)):
    Percentage = Election['Count'][x]/TotalVotes*100
    print(f"{Election['Name'][x]}: {Percentage:.3f}% ({Election['Count'][x]:,})")
    if Election['Count'][x] > MostVotes:
        MostVotes = Election['Count'][x]
        Winner = Election['Name'][x]
print("------------------------------------------")        
print(f"Winner: {Winner}")  
print("------------------------------------------")   

# export results to text file
output_path = os.path.join("Analysis","output.txt")
with open(output_path,'w',newline='') as text_file:
    text_file.write("Election Results \n")
    text_file.write("------------------------------------------ \n")
    text_file.write(f"Total Votes: {TotalVotes:,} \n")
    text_file.write("------------------------------------------ \n")
    MostVotes = Election['Count'][0]
    Winner = Election['Name'][0]
    for x in range(len(Candidates)):
        Percentage = Election['Count'][x]/TotalVotes*100
        text_file.write(f"{Election['Name'][x]}: {Percentage:.3f}% ({Election['Count'][x]:,}) \n")
        if Election['Count'][x] > MostVotes:
            MostVotes = Election['Count'][x]
            Winner = Election['Name'][x]
    text_file.write("------------------------------------------ \n")        
    text_file.write(f"Winner: {Winner} \n")  
    text_file.write("------------------------------------------ \n")  
