import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State



########### Define your variables ######
myheading1='Predicting Home Sale Prices in Ames, Iowa'
image1='ames_welcome.jpeg'
tabtitle = 'Ames Housing'
sourceurl = 'http://jse.amstat.org/v19n3/decock.pdf'
githublink = 'https://github.com/wendi-cui/501-linear-reg-ames-housing'


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div([
                html.H3('Features of Home:'),
                html.Div('Year Built:'),
                dcc.Input(id='YearBuilt', value=2010, type='number', min=2006, max=2010, step=1),
                html.Div('Bathrooms:'),
                dcc.Input(id='Bathrooms', value=2, type='number', min=1, max=5, step=1),
                html.Div('Bedrooms:'),
                dcc.Input(id='BedroomAbvGr', value=4, type='number', min=1, max=5, step=1),
                html.Div('Total Square Feet:'),
                dcc.Input(id='TotalSF', value=2000, type='number', min=100, max=5000, step=1),
                html.Div('Single Family Home:'),
                dcc.Input(id='BldgType_1Fam', value=0, type='number', min=0, max=1, step=1),
                html.Div('Two Family Home:'),
                dcc.Input(id='BldgType_2fmCon', value=0, type='number', min=0, max=1, step=1),
                html.Div('Duplex Home:'),
                dcc.Input(id='BldgType_Duplex', value=0, type='number', min=0, max=1, step=1),
                html.Div('Town House:'),
                dcc.Input(id='BldgType_Twnhs', value=0, type='number', min=0, max=1, step=1),
                html.Div('Town House E:'),
                dcc.Input(id='BldgType_TwnhsE', value=0, type='number', min=0, max=1, step=1),
                html.Div('Large Neighborhood:'),
                dcc.Input(id='LargeNeighborhood', value=0, type='number', min=0, max=1, step=1),

            ], className='four columns'),
            html.Div([
                html.Button(children='Submit', id='submit-val', n_clicks=0,
                                style={
                                'background-color': 'red',
                                'color': 'white',
                                'margin-left': '5px',
                                'verticalAlign': 'center',
                                'horizontalAlign': 'center'}
                                ),
                html.H3('Predicted Home Value:'),
                html.Div(id='Results')
            ], className='four columns')
        ], className='twelve columns',
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4('Regression Equation:'),
    html.Div('Predicted Price = -1363279.4591 + 707.4591*YearBuilt + 13203.447*Bathrooms + -6819.7709*BedroomAbvGr + 48.7927*TotalSF+ 21090.2909*BldgType_1Fam+ 9218.5198*BldgType_2fmCon + -16106.8108*BldgType_Duplex+ -19060.3471*BldgType_Twnhs+ 4858.3473*BldgType_TwnhsE+ -6796.3548*LargeNeighborhood'),
    html.Br(),
    html.A('Google Spreadsheet', href='https://docs.google.com/spreadsheets/d/1q2ustRvY-GcmPO5NYudvsBEGNs5Na5p_8LMeS4oM35U/edit?usp=sharing'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='YearBuilt', component_property='value'),
    State(component_id='Bathrooms', component_property='value'),
    State(component_id='BedroomAbvGr', component_property='value'),
    State(component_id='TotalSF', component_property='value'),
    State(component_id='BldgType_1Fam', component_property='value'),
    State(component_id='BldgType_2fmCon', component_property='value'),
    State(component_id='BldgType_Duplex', component_property='value'),
    State(component_id='BldgType_Twnhs', component_property='value'),
    State(component_id='BldgType_TwnhsE', component_property='value'),
    State(component_id='LargeNeighborhood', component_property='value')

)
def ames_lr_function(clicks, YearBuilt,Bathrooms,BedroomAbvGr,TotalSF,BldgType_1Fam,BldgType_2fmCon,BldgType_Duplex,BldgType_Twnhs,BldgType_TwnhsE,LargeNeighborhood):
    if BldgType_1Fam + BldgType_2fmCon + BldgType_Duplex + BldgType_Twnhs + BldgType_TwnhsE > 1:
        return "please select ONLY ONE house type"
    elif BldgType_1Fam + BldgType_2fmCon + BldgType_Duplex + BldgType_Twnhs + BldgType_TwnhsE == 0:
        return "please select one house type"

    if clicks==0:
        return "waiting for inputs"
    else:
        y = [-1363279.4591 + 707.4591*YearBuilt + 13203.447*Bathrooms + -6819.7709*BedroomAbvGr + 48.7927*TotalSF+ 21090.2909*BldgType_1Fam+ 9218.5198*BldgType_2fmCon + -16106.8108*BldgType_Duplex+ -19060.3471*BldgType_Twnhs+ 4858.3473*BldgType_TwnhsE+ -6796.3548*LargeNeighborhood]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
