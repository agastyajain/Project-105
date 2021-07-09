import pandas as pd
import plotly.express as px
import csv

def get_mean():
    with open("class2.csv",newline="") as f:
        reader = csv.reader(f)
        file_data = list(reader)
    file_data.pop(0)
    total = 0
    for i in file_data:
        total+= float(i[1])
    mean = total / len(file_data)
    print("The mean is : " + str(mean))
    return mean

avg = get_mean()
df = pd.read_csv("class2.csv")
fig = px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes = [dict(type="line",y0=avg,y1=avg,x0=0,x1=30)])
fig.update_yaxes(rangemode = "tozero")
fig.show()