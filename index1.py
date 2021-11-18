import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label('choose a department'),
    dcc.Dropdown(
        id = 'first-dropdown',
        options = [
            {'label':'Computer', 'value' : '1'},
            {'label':'Chemical', 'value' : '2' },
            {'label':'Civil', 'value' : '3'},
            {'label':'ENC', 'value' : '4' },
            {'label':'ECE', 'value' : '5'},
            {'label':'Biotech', 'value' : '6' },
            {'label':'Mechanical', 'value' : '7'},
            {'label':'Mechatronics', 'value' : '8' },
            {'label':'CSED_derabassi', 'value' : '9'},
        ],
        #disabled = True
        placeholder = 'select a department',
        value = 'CSED'
            ),
    html.Div(id='dd-output-container')
    # ),
    
    # html.Br(),
    # html.Br(),
    
    # html.Label('This is a slider'),
    # dcc.Slider(
    #     min = 1,
    #     max = 10,
    #     value =5,
    #     step = .5,
    #     marks = {i: i for i in range(10)}
    #     ),
    
    # html.Br(),
    # html.Br(),
    
    # html.Div([
    #     html.Label('This is an input box'),
    # dcc.Input(
    #     placeholder = 'Input your name',
    #     type = 'text',
    #     value = ''
    #     )
    # ]),
    
    # html.Br(),
    # html.Br(),
    
    # dcc.Textarea(
    # placeholder = 'Input your feedback',
    # value = 'Type your feedback',
    # style = {'width': '100%'}
    # ),
    
    # html.Br(),
    # html.Br(),
    
    # dcc.Checklist(
    # options = [
    #         {'label':'Computer', 'value' : 'CSED'},
    #         {'label':'Chemical', 'value' : 'CHED' }
    #     ],
    #     value = ['CSED','CHED']
    # )
 ])


# app.layout = html.Div([
#     dcc.Dropdown(
#         id='demo-dropdown',
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': 'Montreal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='NYC'
#     ),
#     html.Div(id='dd-output-container')
# ])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(port = 4050)