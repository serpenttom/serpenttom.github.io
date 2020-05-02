import plotly.graph_objects as go
import numpy as np
t=np.linspace(0,2*np.pi,61)
ra=6;
data1=go.Scatter(x=np.cos(t)/ra+3,y=np.sin(t)/ra,line=dict(color='green'))
data2=go.Scatter(x=np.cos(t)/ra+4,y=np.sin(t)/ra,line=dict(color='yellow'))
data3=go.Scatter(x=np.cos(t)/ra+5,y=np.sin(t)/ra,line=dict(color='red'))
data4=go.Scatter(x=np.cos(t)/ra+6,y=np.sin(t)/ra,line=dict(color='green'))
data5=go.Scatter(x=np.cos(t)/ra+7,y=np.sin(t)/ra,line=dict(color='yellow'))
data6=go.Scatter(x=np.cos(t)/ra+8,y=np.sin(t)/ra,line=dict(color='red'))
fig = go.Figure(
    data=[go.Scatter(x=[0,0.5,1,1.5,3], y=[0,0,1,0,0]),data1],
    layout=go.Layout(
        xaxis=dict(range=[0, 9], autorange=False),
        yaxis=dict(range=[-1,5], autorange=False),
        title="Start Title",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=[0,0.5,1  ,1.5,3], y=[0,0,1,  0,0]),data1]),
            go.Frame(data=[go.Scatter(x=[0,0.5,1.5,2.5,4], y=[0,0,0.5,0,0]), data2]),
            go.Frame(data=[go.Scatter(x=[1,1.5,2  ,2.5,4], y=[0,0,1,0,0]),data2]),
            go.Frame(data=[go.Scatter(x=[1,1.5,2.5,3.5,5], y=[0,0,0.5,0,0]),data3]),
            go.Frame(data=[go.Scatter(x=[2,2.5,3  ,3.5,5], y=[0,0,1,0,0]),data3]),
            go.Frame(data=[go.Scatter(x=[2,2.5,3.5,4.5,6], y=[0,0,0.5,0,0]),data4]),
            go.Frame(data=[go.Scatter(x=[3,3.5,4  ,4.5,6], y=[0,0,1,0,0]),data4]),
            go.Frame(data=[go.Scatter(x=[3,3.5,4.5,5.5,7], y=[0,0,0.5,0,0]),data5]),
            go.Frame(data=[go.Scatter(x=[4,4.5,5  ,5.5,7], y=[0,0,1,0,0]),data5]),
            go.Frame(data=[go.Scatter(x=[4,4.5,5.5,6.5,8], y=[0,0,0.5,0,0]),data6]),
            go.Frame(data=[go.Scatter(x=[5,5.5,6  ,6.5,8], y=[0,0,1,0,0]),data6])
])

fig.write_html('worm.html')
