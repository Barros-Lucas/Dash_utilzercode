import datetime
import os
import glob

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State



colors = {
    'background': 'white',
    'text': '#003366'
}


app = dash.Dash()

app.scripts.config.serve_locally = True

app.layout =  html.Div(style={'backgroundColor': colors['background']}, children=[
    #Titre
    html.H1(
        children='Utilzregcode application',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    #Definition du dash
    html.Div(children='A web application to align two pictures, based on a C++ code', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    #Affiche les infos si choix est local
    html.Div(id='info_local',children=[' Assurez vous d\'avoir bien lance le docker avec comme repertoire source un repertoire contenant uniqement les deux images']),
    #Affichage des URLs
    html.Div(id='output-state'),
    html.Div(id='output-start'),
    html.Div(style={#Plus validation du lancement du script
        'width': '100%',
        'height': '60px',
        'textAlign': 'center',
        'margin': 'auto',
        },
        children=[html.Button(id='RUN', n_clicks=0, children='RUN')]),

    html.Div(id='output-final'),
])

#Ecoute du bouton 'RUN' et lance le script
@app.callback(Output('output-final', 'children'),
              [Input('RUN', 'n_clicks')])
def update_output(n_clicks):
        IMGA,IMGB = read_folder()
        #lance le script que si le bouton est clique 1 fois
        if(n_clicks > 0 ):
            print IMGA,IMGB
            cmd = "sh script_local.sh {0} {1}" .format(IMGA,IMGB)
            os.system(cmd)


def read_folder():
    full=""
    full = glob.glob("/home/Dash/*.nii")
    l1= full[0]
    l2= full[1]
    return l1,l2




app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8080,debug=True)
