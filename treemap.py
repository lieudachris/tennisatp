#add a color to the dictionary
color_country['(?)'] = '#e9e9e9'

#create a list of percentages for labeling
Label_per = [str(round(i*100/sum(df_coal.Value),1))+' %' for i in df_coal.Value]

import plotly.express as px
fig = px.treemap(df_coal, path=[px.Constant('2022'), 'Country'],
                 values=df_coal.Percent,
                 color=df_coal.Country,
                 color_discrete_map=color_country,
                 hover_name=Label_per,
                )
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25), showlegend=True)
fig.show()