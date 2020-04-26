import plotly.graph_objects as go

import numpy as np


# Generate curve data
x = [0,1,2,3,4,5,6,7]
y= [6,8,3,2,7,4,5,1]
#x = [0,1,2,3,4]
#y= [3,5,4,2,1]
N = len(x)
yy=list(y)
xm = -1
xM = N
ym =-1
yM =N+1

#s = np.linspace(-1, 1, N)

it=0
l2=[]
x2=[]
ls=[y]
xs=[x]
answer=0
for i in range(0,N):
    for j in range(i+1,N):
        it=it+1
        l2=l2+[[y[i],y[j]]]*2
        if y[i]>y[j]:
            answer=y[i]
            y[i]=y[j]
            y[j]=answer
        ls=ls+[list(y)]*2
        x2=x2+[[i,j]]*2    
ls=ls+[]
# Create figure
data=[go.Bar(x=x, y=yy,name="list",marker=dict(color="blue")),go.Scatter(x=x, y=y,name="list",marker=dict(color="red"))]
#updatem=[dict(type="buttons",bordercolor="orange",buttons=[dict(label="Play",method="animate",args=[])])]
updatem=[dict(
            type="buttons",
            direction="left",
            active=0,            
            buttons=list([dict(label="Play",method="animate",args=[],args2=[])])
            )]
layout=go.Layout(width=720, height=720,
                     xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
                     yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
                     title="Sort",
                     hovermode="closest",
                     updatemenus=updatem)
frame=[go.Frame(data=[go.Bar(x=x, y=ls[k],name="list",marker=dict(color=ls[k+0])),go.Scatter(x=x2[k], y=l2[k])])
                           for k in range(it*2)]
fig = go.Figure(data=data,layout=layout,frames=frame)
fig.update_layout(overwrite=False)
fig.write_html("sort_plotly.html")


