import pandas as pd
import os
 

csvfile = os.path.join("PyPoll", "Resources", "election_data.csv")
 

elec_data = pd.read_csv(csvfile)
 
df_ed = pd.DataFrame(elec_data)
 

percent_count = []
 

candidates = list(df_ed["Candidate"].unique())
 
counts = list(df_ed['Candidate'].value_counts())
 

total_votes = sum(counts)
 

x = 0
 

for candidate in candidates:
    percentage = round(counts[x]/total_votes,3)
    percentage="{:.3%}".format(percentage)
    percent_count.append(percentage)
    x+=1
 

data = list(zip(candidates, percent_count, counts))
 

max_count = df_ed['Candidate'].value_counts()
 

winner_count = max_count.max()
 

df_data = pd.DataFrame(data)
 

winner = list(df_data.loc[df_data[2]== winner_count,0])
 

sorted_data =df_data.columns =["Candidate |", "Percent of Votes |", "Vote Count"]
 

sorted_data = df_data.sort_values("Vote Count", ascending = False )
 

print("Election Results")
print(" -------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"{sorted_data}")
print(f" -------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")
 

 
election_winner = open("election_winner.txt","w")
 
election_winner.write("Election Results\n")
election_winner.write("----------------------------\n")
election_winner.write(f"Total Votes: {total_votes}\n")
election_winner.write(f"--------------------------\n")
election_winner.write(f"{sorted_data}\n")
election_winner.write(f" -------------------------\n")
election_winner.write(f"Winner: {winner}\n")
election_winner.write(f"-------------------------")
 
election_winner.close()