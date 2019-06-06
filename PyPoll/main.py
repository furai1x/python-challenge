import os
import pandas as pd

#  Set directory to current file location

os.chdir(os.path.dirname(__file__)) 

#  Read file in the Resources directory

csv_path = "Resources/election_data.csv"

#  Read csv file into data frame

df_election_data = pd.read_csv(csv_path, encoding="utf-8")

#  Read Total Votes

total_votes = df_election_data["Voter ID"].count()

#  Put summary data into summary data frame

summary_table = df_election_data.groupby(["Candidate"],as_index=False)["Voter ID"].count().sort_values(["Voter ID"], ascending=False)

summary_table.rename(columns={"Voter ID":"Number of Votes"}, inplace=True)

#  Calculate the percent of votes

percent_votes = summary_table["Number of Votes"]/total_votes*100

#  Add column with percent of votes

summary_table["Percent of Votes"] = percent_votes
summary_table["Percent of Votes"] = summary_table["Percent of Votes"].round(3)

vote_summary_table = summary_table.reset_index(drop=True)

# Export Results to file

csv_path = "Output/election_summary.csv"

vote_summary_table.to_csv(csv_path, encoding="utf-8",index=False)


#  

summary_output = vote_summary_table["Candidate"] + ":  " + vote_summary_table["Percent of Votes"].map(str) + "00%  (" + vote_summary_table["Number of Votes"].map(str) + ")" 
   
# Print output

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(summary_output.to_string(header=False,index=False))
print("-------------------------")
print("Winner:  " + summary_table["Candidate"].head(1).item())


