import os
import pandas as pd

#  Set directory to current file location

os.chdir(os.path.dirname(__file__)) 

#  Read file in the Resources directory

csv_path = "Resources/budget_data.csv"

#  Read csv file into data frame

df_budget_data = pd.read_csv(csv_path, encoding="utf-8")

total_months = len(df_budget_data["Date"].unique())

#  Initialize "Previous" column list

prev_prof_loss = [0]

#  Add the previous period profit/loss value to list

prev_prof_loss += [row for row in  (df_budget_data["Profit/Losses"].head(total_months-1))]

#  Add the Previous list to the data frame

df_budget_data["Previous"]= prev_prof_loss

#  Calculate the change in profit/losses for each period

df_budget_data["Change"] = df_budget_data["Profit/Losses"]-df_budget_data["Previous"]

#  Build output

total_prof_loss = df_budget_data["Profit/Losses"].sum()
avg_change = round(df_budget_data["Change"].tail(total_months-1).mean(), 2)
max_change = df_budget_data["Change"].tail(total_months-1).max()
max_change_date = df_budget_data.loc[df_budget_data["Change"]==max_change, "Date"].item()
min_change = df_budget_data["Change"].tail(total_months-1).min()
min_change_date = df_budget_data.loc[df_budget_data["Change"]==min_change, "Date"].item()

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total ${total_prof_loss}")
print(f"Average Change {avg_change}")
print(f"Greatest Increase in Profits: {max_change_date} $({max_change})")
print(f"Greatest Decrease in Profits: {min_change_date} $({min_change})")






summary_table = pd.DataFrame({"Total Months":  total_months, 
                              "Total $": [total_prof_loss], 
                              "Average Change": [avg_change], 
                              "Greatest Increase in Profits Month": [max_change_date],
                              "Greatest Increase in Profits": [max_change], 
                              "Greatest Decrease in Profits Month": [min_change_date],
                              "Greatest Decrease in Profits":  [min_change]})

csv_path = "Resources/budget_summary.csv"

summary_table.to_csv(csv_path, encoding="utf-8")