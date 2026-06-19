import pandas as pd

#print(pd.__version__)

#Series = pandads 1 dimensional labeled array that can hold any data type

#data = [100, 200, 104, 400, 60]
#series = pd.Series(data, index =["a", "b", "c", "d", "e"]) #setting custom indexes

#print(series) #prints index and meta-data, also shows data type (in this case int64), decimals would be float64, strings would be object

#print(series.loc["a"]) #returning the value at whatever the label is iloc = integer location e.g[0]

#print(series[series <= 200])

calories = {"Day1": 1750, "Day2": 2100, "Day3": 1700} #Dictionary

series = pd.Series(calories)

#series.loc["Day3"] += 500 #adding an additional 500 calories to location Day 3

print(series[series >= 2000]) 







