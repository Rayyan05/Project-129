import csv
import pandas as pd

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'

df1 = []
df2 = []

with open(file1,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        df1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        df2.append(i)

h1 = df1[0]
h2 = df2[0]

p_d1 = df1[1:]
p_d2 = df2[1:]

h = h1+h2
p_d = []

for i in p_d1:
    p_d.append(i)

for j in p_d2:
    p_d.append(j)

with open("total_stars.csv",'w',encoding='utf8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(p_d)
    

df = pd.read_csv("total_stars.csv")
df.tail(8)

