import pandas as pd

#reducing a set of values intoa single summary value - used to summarise and analyse data
#often used with groupby() function

df = pd.read_csv("Pokemon Stats.csv")

print(df.mean(numeric_only = True)) #finding the mean of any columns that are numbers
print(df.sum(numeric_only= True))
print(df.min(numeric_only=True))

print(df.count()) #counting number of values 
#Single Column

print("\n")
print(df["Defense"].mean(numeric_only = True))
print(df["Defense"].sum(numeric_only= True))
print(df["Defense"].min(numeric_only=True))

#USING PRINT BY

group = df.groupby("Type 1")

print(group["Attack"].mean())

