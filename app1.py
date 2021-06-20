DB_HOST = 'ec2-54-74-14-109.eu-west-1.compute.amazonaws.com'
DB_NAME = "de0fglpocdb2up"
DB_USER = "jgpjdpqktnjurl"
DB_PASS = "479cbe7cb2935b6151a1145e1bce96e7575bcecfd5d581ea214210358d1b0172"

from datetime import datetime

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
import psycopg2
import psycopg2.extras

from data import suka

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) as conn:
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute("SELECT * FROM raport_month;")
#     data_table = cur.fetchall()
#
#     cur.execute("SET timezone = 'Asia/Sakhalin';")
#
#     # запрос таблицы
#     data_table_base = pd.DataFrame(data_table, columns=['отряд', 'Пожарная часть', 'Пожарная техника', 'Номер', 'Месяц',
#                                                         'Вид топлива', 'Норма общего пробега', 'Общий пробег с '
#                                                                                                'начала эксплуатации',
#                                                         'Работа с насосом', 'Работа без насоса',
#                                                         'Фактический расход', 'Пробег', 'Нормативный расход',
#                                                         'Показание спидометра начало месяца', 'Показание спидометра '
#                                                                                               'конец месяца',
#                                                         'общий пробег месяц'])

html.Div(className='neumorphism-box')

app.layout = html.Div([

    html.Div([
        html.Div([
            html.Div('New Blog', className='primary text'),
            html.Div('Read it now!', className='secondary text')
        ], className='btn blog-button')
    ], className='neumorphism-box'),

    html.Div(html.H3('Отчет ГСМ за месяц'), className='title'),

    html.Div([

        html.Form([

            dcc.Dropdown(id='dropdown_month',
                         options=[{'label': a, "value": a} for a in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],
                         value=6, placeholder="Выберите номер месяцв", searchable=True,
                         className='department_dropdown'),
            html.Br(),

            dcc.Dropdown(id='dropdown_department',
                         options=[{'label': a, "value": a} for a in
                                  ['А-Сахалинский', 'Анива', 'Долиск', 'Курильск', 'Макаров', 'Невельск', 'Новиково',
                                   'Поронайск', 'С-Курильск', 'Томари', 'Тымовское', 'Углегорск', 'Чехов', 'Ю-Курильск',
                                   'Смирных']],
                         value='Макаров', placeholder="Выберите название отряда", searchable=True,
                         className='department_dropdown'),
            html.Br(),

            dcc.RadioItems(
                id='dropdown_fuel_type',
                options=[{'label': a, "value": a} for a in ['Дизельное топливо', 'Бензин А-92', 'Бензин А-80']],
                value='Дизельное топливо',
                labelStyle={'display': 'inline-block'}
            ),
            html.Br(),

            dash_table.DataTable(
                id='raport_month_table',
                columns=[{"name": c, "id": c} for c in
                         ['Пожарная часть', 'Пожарная техника', 'Номер',
                          'Показание спидометра на начало месяца',
                          'Показание спидометра на конец месяца', 'Пробег', 'Работа с насосом', 'Работа без насоса',
                          'Фактический расход', 'Нормативный расход']],
                page_size=25,
                data=[],
                style_cell={
                    'minWidth': '41px', 'width': '41px', 'maxWidth': '55px',
                    'whiteSpace': 'normal'
                },
                style_header={
                    'fontWeight': 'bold'
                },

                style_cell_conditional=[

                    {'textAlign': 'center'},

                ],
                sort_action='native',
                style_data_conditional=[
                    {
                        'if': {
                            'filter_query': '{общий пробег от нормы, %} > 32',
                            'column_id': 'общий пробег от нормы, %'
                        },
                        'color': 'tomato',
                        'fontWeight': 'bold'
                    }]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            dash_table.DataTable(
                id='raport_month_table2',
                columns=[{"name": c, "id": c} for c in
                         ['Пожарная часть', 'Пожарная техника', 'Номер', 'Общий пробег месяц',
                          'Норма общего пробега год', 'Общий пробег с начала года',
                          'Общий пробег с начала эксплуатации', 'Расход ГСМ месяц', 'Расход ГСМ с начала года',
                          'Заправка ГСМ месяц', 'Заправка ГСМ год']],
                page_size=25,
                data=[],
                style_cell={
                    'minWidth': '41px', 'width': '41px', 'maxWidth': '55px',
                    'whiteSpace': 'normal'
                },
                style_header={
                    'fontWeight': 'bold'
                },

                style_cell_conditional=[

                    {'textAlign': 'center'},

                ],
                sort_action='native',
                style_data_conditional=[
                    {
                        'if': {
                            'filter_query': '{общий пробег от нормы, %} > 32',
                            'column_id': 'общий пробег от нормы, %'
                        },
                        'color': 'tomato',
                        'fontWeight': 'bold'
                    }]),
            dcc.Store(id="store1", data=0),
            html.Div(dcc.Interval(id='interval_page', interval=4000))

        ], className='second_columns'),

    ], className='first_line'),

], className='body')


@app.callback(
    [dash.dependencies.Output('raport_month_table', 'data'),

     dash.dependencies.Output('raport_month_table2', 'data'),
     ],
    [dash.dependencies.Input("interval_page", "n_intervals"),
     dash.dependencies.Input('dropdown_month', 'value'),
     dash.dependencies.Input('dropdown_department', 'value'),
     dash.dependencies.Input('dropdown_fuel_type', 'value'),
     ],
    [dash.dependencies.State('raport_month_table', 'data'),
     dash.dependencies.State('raport_month_table2', 'data'),
     dash.dependencies.State('store1', 'data')
     ], prevent_initial_call=True
)
def raport_month_table(n_intervals, dropdown_month, dropdown_department, dropdown_fuel_type, raport_month_table,
                       raport_month_table2, data):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM base_table_aggregate;")
        data_table = cur.fetchall()

        cur.execute("SELECT * FROM aggregate_mileage;")
        data_table2 = cur.fetchall()

        cur.execute("SET timezone = 'Asia/Sakhalin';")

        # запрос таблицы
        data_table_base = pd.DataFrame(data_table,
                                       columns=['Пожарная часть', 'Пожарная техника', 'Номер', 'Вид топлива',
                                                'Отряд', 'Номер месяца', 'Пробег',
                                                'Работа с насосом', 'Работа без насоса',
                                                'Фактический расход', 'Нормативный расход', 'Показание спидометра на '
                                                                                            'начало месяца',
                                                'Показание спидометра на конец месяца', 'Проверка пробега'])

        raport_month_table = \
            data_table_base[
                (data_table_base['Номер месяца'] == dropdown_month) & (
                        data_table_base['Отряд'] == dropdown_department) & (
                        data_table_base['Вид топлива'] == dropdown_fuel_type)][
                ['Пожарная часть', 'Пожарная техника', 'Номер', 'Отряд', 'Номер месяца', 'Пробег',
                 'Работа с насосом', 'Работа без насоса', 'Фактический расход', 'Нормативный расход',
                 'Показание спидометра на начало месяца', 'Показание спидометра на конец месяца']]

        # запрос таблицы
        data_table_base2 = pd.DataFrame(data_table2,
                                        columns=['Пожарная часть', 'Пожарная техника', 'Номер',
                                                 'Отряд', 'Номер месяца', 'Общий пробег месяц',
                                                 'Норма общего пробега год', 'Общий пробег с начала года',
                                                 'Общий пробег с начала эксплуатации', 'Расход ГСМ месяц',
                                                 'Расход ГСМ с начала года', 'Заправка ГСМ месяц', 'Заправка ГСМ год'])

        raport_month_table2 = \
            data_table_base2[
                (data_table_base2['Номер месяца'] == dropdown_month) & (
                        data_table_base2['Отряд'] == dropdown_department)][
                ['Пожарная часть', 'Пожарная техника', 'Номер', 'Общий пробег месяц', 'Норма общего пробега год',
                 'Общий пробег с начала года', 'Общий пробег с начала эксплуатации', 'Расход ГСМ месяц',
                 'Расход ГСМ с начала года', 'Заправка ГСМ месяц', 'Заправка ГСМ год']]

    return raport_month_table.to_dict('records'), raport_month_table2.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
