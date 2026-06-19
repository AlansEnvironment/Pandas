import pandas as pd

#Data Frame is a tabular 2D data structure with rows and columns 

data = {"Name": ["Mother", "Father", "Son", "Daughter"],
        "Age": [57, 60, 22, 17]
        }

#data frame (Df)
df = pd.DataFrame(data, index = ["Occupant 1", "Occupant 2", "Occupant 3", "Occupant 4"])
print(df)
print(df.loc["Occupant 2"])
print(df.iloc[2])

#adding a new column
df["Job"] = ["Nurse", "Engineer", "Student", "Student"]
#adding a new row
new_row = pd.DataFrame([{"Name": "Uncle", "Age": 60, "Job": "Electrician" },
                        {"Name": "Aunty", "Age": 60, "Job": "Teacher" }], index=["Guest 1", "Guest 2"])
df = pd.concat([df, new_row])

print(df)


