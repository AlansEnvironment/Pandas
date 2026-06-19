import pandas as pd

df = pd.read_csv("Pokemon Stats.csv", index_col= "Name")
# Keeping the rows that match a condition

#Weak_pokemon = df[df["Attack"] <= 70]
#print(Weak_pokemon)

Legendary_poke = df[df["Legendary"] == True]
print(Legendary_poke)

Water_pokemon = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]
print(Water_pokemon)

fire_fly = df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]
print(fire_fly)






