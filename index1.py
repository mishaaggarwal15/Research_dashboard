import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash()

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
    
    # html.Br(),
    # html.Br(),
    
    # html.Label('This is a slider'),
    # dcc.Slider(
    #     min = 1,
    #     max = 10,
    #     value = 5,
    #     step = .5,
    #     marks = {i: i for i in range(1, 10)}
    # ),
    
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

@app.callback(
    Output('dd-output-container', 'children'),
    Input('first-dropdown', 'value')
)
def update_output(value):
    dept = ['CSED', 'CSED_derabassi', 'Chemical', 'EIC', 'ECE', 'Mechanical', 'Biotech', 'Civil', 'Distant_Edu']
    extension = '.csv'
    filename = value + extension

    df = pd.read_csv('final_data/{}'.format(filename))
    sum = df['count'].sum()

    return 'The Department {} has published {} research papers.'.format(dept[int(value)], sum)
    

if __name__ == '__main__':
    app.run_server(debug=True)
