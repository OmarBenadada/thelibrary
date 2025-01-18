import pandas as pd
df=pd.read_csv("thelibraryy.csv")
i=0
listo=[]
while df.shape[0]>i:
    listo.append(f'the book  {df["Title"][i]}  by  {df["Author"][i]}  written in  {df["Year"][i]}  and its  {df["Genre"][i]}')
    i+=1
print(listo)    