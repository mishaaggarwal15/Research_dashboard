import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output


app = dash.Dash()
sum = []
def tab_layout(name, fig_plot, out_table):
    layout = html.Div([
    html.H3(name, style={'text-align':'center'}),
    html.Div([
        html.Div([fig_plot 
        ],),
        html.Br(),
        html.Div([
    html.H4('Prediction for next 14 days', style={'text-align':'center'})]),
        html.Div([out_table]),
        html.Div([
            html.H6(id='page-3-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
    return layout


@app.callback(
    Output('dd-output-container', 'children'),
    Input('first-dropdown', 'value')
)
def update_output(value):
    # dept = ['CSED', 'CSED_derabassi', 'Chemical', 'EIC', 'ECE', 'Mechanical', 'Biotech', 'Civil', 'Distant_Edu']
    # extension = '.csv'
    # filename = value + extension

    # df = pd.read_csv('final_data/{}'.format(filename))
    # sum = df['count'].sum()

    # return 'The Department {} has published {} research papers.'.format(dept[int(value)], sum)
    # sum = []
    sum.clear()
    for i in range(9):
        x = str(i)
        extension = '_2018.csv'
        filename = x + extension

        df = pd.read_csv('final_data/{}'.format(filename))
        sum.append(df['count'].sum())
        
    return sum[int(value)]

dept = ['CSED', 'CSED_derabassi', 'Chemical', 'EIC', 'ECE', 'Mechanical', 'Biotech', 'Civil', 'Distant_Edu']

app.layout = html.Div([
    # html.Label('choose a department'),
    dcc.Dropdown(
        id = 'first-dropdown',
        options = [
            {'label':'CSED', 'value' : '0'},
            {'label':'CSED_derabassi', 'value' : '1'},
            {'label':'Chemical', 'value' : '2' },
            {'label':'EIC', 'value' : '3'},
            {'label':'ECE', 'value' : '4' },
            {'label':'Mechanical', 'value' : '5'},
            {'label':'Biotech', 'value' : '6' },
            {'label':'Civil', 'value' : '7'},
            {'label':'Distant_Edu', 'value' : '8' },
            
        ],
        #disabled = True
        placeholder = 'Select a Department',
        value = '0'
            ),
    html.Div(id='dd-output-container'),
    # ),
    dcc.Graph(
    figure={
        'data': [
            {'x': ['CSED', 'CSED_derabassi', 'Chemical', 'EIC', 'ECE', 'Mechanical', 'Biotech', 'Civil', 'Distant_Edu'], 'y': sum, 'type': 'bar', 'name': 'SF'},
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }
    }
    ),
    html.Div([
    dcc.Tabs(id='tabs', value=dept[0], children=[
        dcc.Tab(label= dept[0], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[1], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[2], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[3], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[4], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[5], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[6], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[7], style={'textAlign': 'right'}),
        dcc.Tab(label= dept[8], style={'textAlign': 'right'}),
        ], vertical=True,parent_style={'float': 'left'}),
        html.Div(id='tabs-content', style={'width': '75%', 'float': 'left'})
    ]),
   
 ])
# fig_plot = html.Div(id='fig_plot')
# out_table = html.Div(id='out_table')
# @app.callback(Output('tabs-content', 'children'),
#               [Input('tabs', 'value')])
# def render_content(tab):
#     if tab == dept[0]:
#         return tab_layout(dept[0], fig_plot, out_table)
        
#     elif tab == dept[1]:
#         return tab_layout(dept[1], fig_plot, out_table)
        
#     elif tab == dept[2]:
#         return tab_layout(dept[2], fig_plot, out_table)
        
#     elif tab == dept[3]:
#         return tab_layout(dept[3], fig_plot, out_table)
        
#     elif tab == dept[4]:
#         return tab_layout(dept[4], fig_plot, out_table)
        
#     elif tab == dept[5]:
#         return tab_layout(dept[5], fig_plot, out_table)
        
#     elif tab == dept[6]:
#         return tab_layout(dept[6], fig_plot, out_table)
        
#     elif tab == dept[7]:
#         return tab_layout(dept[7], fig_plot, out_table)

if __name__ == '__main__':
    app.run_server(debug=True)