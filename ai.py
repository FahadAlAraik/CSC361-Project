import pandas as pd
exel=pd.read_excel("E:/games/minecraft/cities (1).xlsx",sheet_name="Sheet2")
cities_dic={}
for i in range(len(exel)):
    cities_dic[exel.loc[i][0]] = []

for i in range(len(exel)):
       cities_dic[exel.loc[i][0]].append([exel.loc[i][1], float (exel.loc[i][2])])
print(cities_dic)
print("fjfaslka;fa")
#asfdadadasdadsd