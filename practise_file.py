
import pandas as pd

# Create an empty dataset
df = pd.DataFrame()

# Print the dataframe
print(df)

# Load an excel dataset(games_details)
df = pd.read_csv("C:/Users/Bin Zheng/Desktop/py/ranking.csv",encoding="utf-8")

# print the dataframe again.
print(df)

print(df.head(5))

print(df[:3])

df = df[:3]

team = df.TEAM
print(team)

win = df.W
print(win)

import matplotlib.pyplot as plt
# Create a bar graph
plt.bar(team, win)
plt.title("Teams & Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.show()

# Create a line graph
plt.plot(team, win)
plt.title("Teams & Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.show()













