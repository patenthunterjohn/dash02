# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash, dash_table, html
import dash_bootstrap_components as dbc
import warnings

# 載入資料
df_query = pd.read_excel('Meta專利透視元宇宙技術-dash.xlsx')  # 請替換成正確檔名

# 將 "公開/公告日" 欄位轉換為字串格式
df_query['公開/公告日'] = df_query['公開/公告日'].astype(str)

# 儀表板設定
def tool_show_table(df_query):
    return dash_table.DataTable(
        data=df_query.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df_query.columns],
        page_size=10,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        cell_selectable=True,

        style_cell_conditional=[
            {'if': {'column_id': '描述'}, 'width': '50%'},
        ],

        style_header={
            'font-family': 'Times New Roman',
            'font-weight': 'bold',
            'text-align': 'center',
            'backgroundColor': 'rgb(30, 30, 30)',
        },
        style_data={
            'font-family': 'Times New Roman',
            'text-align': 'center',
            'whiteSpace': 'normal',
            'height': 'auto',
            'lineHeight': '15px',
            'color': 'black',
            'backgroundColor': 'white',
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',
            }
        ],
        style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'},
        style_filter={'backgroundColor': '#FFFFE0', 'color': 'black'},
    )

# 忽略警告
warnings.filterwarnings("ignore", category=UserWarning)

# 建立 Dash 應用
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 設定 Layout
app.layout = html.Div([
    html.Div(tool_show_table(df_query))
])

# 執行 Dash 應用
if __name__ == "__main__":
    app.run_server(debug=True)
