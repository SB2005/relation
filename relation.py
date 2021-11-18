import pandas as pd 
import plotly.express as px
import numpy as np 


def findCorrelation(data,x,y):
    x_list = data[x].tolist()
    y_list = data[y].tolist()
    correlation = np.corrcoef(x_list,y_list)
    print(correlation[0,1])

def plotFigure(data,x,y):
    fig = px.scatter(data,x=x,y=y)
    fig.show()

def getData():
    df = pd.read_csv('tv.csv')
    column_x = "Size of TV"
    column_y = "Average time spent watching TV in a week"
    findCorrelation(df,column_x,column_y)
    plotFigure(df,column_x,column_y)

getData()