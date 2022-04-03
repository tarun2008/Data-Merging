import pandas as pd
import csv
df = pd.read_csv("dwarf_stars.csv")
df = df.dropna()
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.to_csv("unit_converted_dwarf_stars.csv")

data1 = []
data2 = []

with open('bright_star.csv','r') as f:
    reader = csv.reader(f)
    for row in reader :
        data1.append(row)
with open('unit_converted_dwarf_stars.csv','r') as f:
    reader = csv.reader(f)
    for row in reader :
        data2.append(row)

headers1 = data1[0]        
planet_data1 = data1[1:]
headers2 = data2[0]        
planet_data2 = data2[1:]
headers = headers1+headers2
planet_data = []

for index,datarow in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("final.csv", "a+") as f:
     csvwriter = csv.writer(f)
     csvwriter.writerow(headers)
     csvwriter.writerows(planet_data)          