import pandas as pd

df = pd.read_csv("Pokemon Stats.csv")

#1 Dropping irrelevant columns
#df = df.drop(columns=["Legendary", "#", "Total"])

#print(df)

#Handling Missing Data
#df = df.dropna(subset=["Type 2"])

#instead of dropping them we replace 

#df = df.fillna({"Type 2": "None"})
#Fixing inconsistent values
df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS",
                                     "Fire": "FIRE",
                                     "Water": "WATER"})

#df["Name"] = df["Name"].str.lower() #makes all of the characters lowercase

#Fixing data type
df["Legendary"] = df["Legendary"].astype(bool)

#Fixing Duplicate Entries
#df = df.drop_duplicates()

print(df.to_string())