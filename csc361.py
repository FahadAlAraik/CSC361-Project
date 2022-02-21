import pandas as pd



citiesForVetrices = pd.read_excel("C:/Users/Fahad/Documents/cities.xlsx", sheet_name="Sheet1")

data = pd.read_excel("C:/Users/Fahad/Documents/cities.xlsx", sheet_name="Sheet2")
cities_dic = {}
var = 0
for i in range(len(data)):
    cities_dic[data.loc[i][0]] = []

for i in range(len(data)):
       cities_dic[data.loc[i][0]].append([data.loc[i][1], float(data.loc[i][2])])


print(type(cities_dic['Riyadh'][0][1]))
test = True
