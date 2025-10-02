import pandas as pd 
import matplotlib.pyplot as mp
vs=pd.read_csv("gender_submission.csv")

#Rename the columns name

vs.rename(columns={"PassengerId":"Id","Survived":"Status"},inplace=True)
print(vs)

#Explore the Dataset

print(vs.head())
print(vs.tail())
print(vs.info())
print(vs.shape)

#Filter Data

top_10_servivors=vs[vs["Status"]==1].head(10)
top_10_non_servivors=vs[vs["Status"]==0].head(10)
print(f"Top 10 servivors:\n {top_10_servivors}")
print(f"Top 10 non servivors:\n {top_10_non_servivors}")

#count Data

count=vs["Status"].value_counts()
print(count)

#count servivors and non servivors

count_servivors=len(vs[vs["Status"]==1])
count_non_servivors=len(vs[vs["Status"]==0])
print(f"count of servivors:\n {count_servivors}")
print(f"count of non servivors:\n {count_non_servivors}")

#calculate percentages

Total=len(vs)
print(f"Total servivors and non servivors :{Total}")
perservivors=(count_servivors/Total)*100
pernonservivors=(count_non_servivors/Total)*100
print(f"Percentage Survived:{perservivors:.2f}")
print(f"percentage Non Survived:{pernonservivors:.2f}")

#Visualize Results

count.plot(kind='bar',color=["blue","black"])
mp.xlabel("status")
mp.ylabel("Number of People")
mp.title("Survived vs Not Survived")
mp.show()