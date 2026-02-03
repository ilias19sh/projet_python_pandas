import pandas as pd 

df= pd.read_csv("../data/rating.csv")

print(df.sample(10))