# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import dash
import dash_bootstrap_components as dbc
import sqlite3
import plotly.express as px
import pandas as pd 
from dash import dcc


conexao = sqlite3.connect("db/loja1.db")

script = "SELECT * FROM PRODUTOS"

dados = pd.read_sql(script, conexao)

fornecedor_vs_vlr = dados.groupby("FORNECEDOR")["VLRPROD"].sum()
fornecedor_vs_vlr = fornecedor_vs_vlr.reset_index()

fornecedor_vs_qtd = dados.groupby("FORNECEDOR")["QTDPROD"].sum()
fornecedor_vs_qtd = fornecedor_vs_qtd.reset_index()

nomeprod_vs_qtd = dados.groupby("NOMEPROD")["QTDPROD"].sum()
nomeprod_vs_qtd = nomeprod_vs_qtd.reset_index()

fig_vs_vlr = px.bar(fornecedor_vs_vlr, x="FORNECEDOR", y="VLRPROD")
fig_vs_qtd = px.pie(fornecedor_vs_qtd, names="FORNECEDOR", values="QTDPROD")
fig_name_vs_qtd = px.bar(nomeprod_vs_qtd, x="NOMEPROD", y="QTDPROD")


app = dash.Dash(__name__)

app.layout = dbc.Container([
    dcc.Graph(figure = fig_vs_vlr),
    dcc.Graph(figure = fig_vs_qtd),
    dcc.Graph(figure = fig_name_vs_qtd)
])

if __name__ == "__main__":
    app.run(debug=True)

app.layaut = dcc= connect
dcc.Graph(fig_name_vs_qtd)
 app.ru(debug)True 













