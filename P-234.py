import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as ply 
import plotly.graph_objects as go 
import plotly.express as px
dataset = pd.read_csv("projectC234_EPL.csv")
gc = dataset["Goals"]
scao = gc.groupby(dataset["Club"])
suma = scao.sum()
sorteda = suma.sort_values(ascending = False)
print("premier league goals: ",sorteda)
e = dataset.sort_values(by = ["Goals"],ascending = False)[:10]
print(e)
fig = px.bar(e,x='name',y="Goals",color="Goals")
fig.show()