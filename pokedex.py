import pandas as pd

df = pd.read_csv("Pokemon Stats.csv", index_col = "Name") #800 rows by 13 Columns
#reading a json file pd.read_json("name or pathfile")
# print(df) #add df.to_string() --> to print out all the data instead of the truncated version

#Selection by Column

#print(df["Name"].to_string())
#print(df["Generation"])

#print(df[["Name", "Type 1", "Type 2"]])

#Selection by rows
#print(df.loc["Bulbasaur":"Greninja", ["HP", "Attack", "Defense"]]) #selecting a range of rows and selected attributes

#integer based selection
#print(df.iloc[0:11:2, 0:4])

#--------------------------------EXERCISE---------------------------------------#
print("\nWelcome to Pokemon Index, Please type pokemon name and Stats that you would like to see")
print("Stats are: Type 1, Type 2, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Generation, Legendary: 10 in total \n")
print("CASE AND SPACE SENSITIVE")

pokemon = input("Enter a Pokemon name: ")



stats1 = input("What first stats would you like to display: ")
stats2 = input("What second stats would you like to display: ")
stats3 = input("What third stats would you like to display: ")
stats = stats1, stats2, stats3

try:
    print(df.loc[pokemon, stats])
except KeyError:
    print(f"{pokemon} not found")
    print(f"{stats} make sure to type the proper stats")


#I AM VERY SURE THERE IS MORE EFFICIENT AND user friendly way to do all of this





