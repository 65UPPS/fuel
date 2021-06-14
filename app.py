from flask_sqlalchemy import SQLAlchemy

DB_HOST = 'ec2-54-229-68-88.eu-west-1.compute.amazonaws.com'
DB_NAME = "d6br3mamlectc2"
DB_USER = "rtzklqyvvpdqcf"
DB_PASS = "8f33893cccc6db6294049a9cb3eebd05ac2ef2c946f9c3c241b8ce45a9b6afe5"

import datetime
from datetime import date
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

# print(str(time))
#
# c = datetime.strptime('03:55', '%H:%M').time()
# 5
# print(c)
#
# list_my = {
#     '4826 СМ': ['Снегоход'],
#     '4827 СМ': ['Снегоболотоход'],
#     'А 868 РУ': ['ЗИЛ(131)'],
#     'К 136 ТК': ['АЦ-7,5-40(4320)'],
#     'К 441 РТ': ['АЦ-2,5-40(5313)'],
#     'М 063 НХ': ['АЦ-5,5-40(5557)'],
#     'М 355 НЕ': ['АЦ-5,5-40(5557)'],
#     'М 367 НЕ': ['АРС(15)'],
#     'М 368 ТК': ['АЦЛ-3,0-40-17(43118)'],
#     'М 736 ВМ': ['УАЗ(390995)'],
#     'М 910 МЕ': ['АМУР(531382)'],
#
# }
#
#
# df = pd.DataFrame.from_dict(list_my, orient='index', columns=['auto'])

# dbc.Col(dcc.Dropdown(id='dropdown_osp',
#                      options=[{'label': a, "value": a} for a in
#                               list.keys()],
#                      value='Анива'), style={'text-align': 'left', 'font-size': 'large'},
#         width={'size': 3, "offset": 0, 'order': 0}),
#
# dbc.Col(dcc.Dropdown(id='dropdown_psch',
#                      options=[{'label': b, "value": b} for b in
#                               df['Пожарная часть'].unique()],
#                      value=''), style={'text-align': 'left', 'font-size': 'large'},
#         width={'size': 3, "offset": 0, 'order': 0}),


# with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) as conn:
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute("SELECT count(*) FROM total_consumption_join_main4;")
#     data = cur.fetchall()
#     print(data)


# app.server.config["SQLALCHEMY_DATABASE_URI"] = \
#     'postgresql://tinwqzwytvlios:4914678fe9df3d09af79ff8471077cdde4616e7400a3ab8f0312e41817566821@ec2-63-34-97-163.eu' \
#     '-west-1.compute.amazonaws.com:5432/dahabnlnvjhvm7'
# #
# db = SQLAlchemy(app.server)
#
# df = pd.read_sql_table('productlist', con=db.engine)
# with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) as conn:
#     cur = conn.cursor()
#     count_str = cur.execute('SELECT * FROM productlist;')


app.layout = html.Div([
    html.Div([
        html.Form([
            html.Div([

                # Пожарный отряд
                # html.Pre('Пожарный отряд:'),
                html.Pre('Введите данные:', className='login_name'),
                dcc.Dropdown(id='brigate', options=[{'label': a, "value": a} for a in suka.keys()],
                             value='Макаров', placeholder="Выберите название отряда", searchable=True),
                # html.Span('Это поле должно содержать E-Mail в формате example@site.com', className='form__error'),
                # Пожарная часть
                # html.Pre('Пожарная часть:'),
                dcc.Dropdown(id='values', options=[], placeholder="Выберете название ПЧ"),
                # html.Span('Это поле должно содержать текстовое значение', className='form__error'),

                # Календарь
                # html.Pre('Дата выезда (м/д/г):'),
                html.Div(dcc.DatePickerSingle(id='calendar', month_format='MMMM Y', placeholder='MMMM Y', date=date(
                    datetime.now().year, datetime.now().month, datetime.now().day), first_day_of_week=1),
                         className='first_date'),

                # Время выезда
                # html.Pre('Время выезда:'),
                dbc.Input(id='time_out', type="text", placeholder="Время выезда", value='08:00', required=True,
                          autoComplete='off'),

                # Пожарная техника
                # html.Pre('Пожарная техника:'),
                dcc.Dropdown(id='fire_auto', placeholder="Вид техники", options=[],
                             style={'background-color': '#e6e3df'}),

                # Государственный номер
                # html.Pre('Государственный номер:'),
                dcc.Dropdown(id='gov_number', placeholder="Государственный номер", value="",
                             style={'background-color': '#e6e3df'}, options=[]),

                # Показание спидометра при выезде
                # html.Pre('Показание спидометра при выезде:'),
                dbc.Input(id='speedometr_start', type="number", placeholder="Показание спидометра при выезде",
                          required=True, autoComplete='off'),

                # Показание спидометра при возвращении
                # html.Pre('Показание спидометра при возвращении:'),
                dbc.Input(id='speedometr_end', type='number', placeholder="Показание спидометра на момент прибытия",
                          required=True, autoComplete='off'),

                # Работа с насосом, мин
                # html.Pre('Работа с насосом, мин:'),
                dbc.Input(id='work_pump', type="number", placeholder="Работа с насосом", required=True,
                          autoComplete='off'),

                # Работа без насоса, мин
                # html.Pre('Работа без насоса, мин:'),
                dbc.Input(id='without_pump', type="number", placeholder="Работа без насоса", required=True,
                          autoComplete='off'),

                # Фактический расход топлива, л
                # html.Pre('Фактический расход топлива, л:'),
                dbc.Input(id='department4', type="number", placeholder="Фактический расход", required=True,
                          autoComplete='off'),

                # Дата возвращения (м/д/г)
                # html.Pre('Дата возвращения (месяц/день/год):'),
                html.Div(dcc.DatePickerSingle(id='date_return', month_format='MMMM Y', placeholder='MMMM Y', date=date(
                    datetime.now(
                    ).year, datetime.now().month, datetime.now().day), first_day_of_week=1, className="date_return")),

                # Время возвращения
                # html.Pre('Время возвращения:'),
                dbc.Input(id='time_return', type="text", placeholder="Время возвращения", value='08:00', required=True,
                          autoComplete='off'),

                # Основание выезда
                # html.Pre('Основание выезда:'),
                dbc.Input(id='reason_leaving', type="text", placeholder="Основание для выезда", required=True,
                          autoComplete='off'),

            ], className='form__field'),
            html.Div(

                html.Button('Сохранить', id='save_to_postgres', n_clicks=0), className='footer_form'),
        ], className='form'),

        html.Form([

            dcc.Dropdown(id='brigate2', options=[{'label': a, "value": a} for a in suka.keys()],
                         value='Макаров', placeholder="Выберите название отряда", searchable=True,
                         className='department_dropdown'),
            html.Br(),

            dash_table.DataTable(
                id='the_table',
                columns=[{"name": c, "id": c} for c in
                         ['дата', 'отряд', 'часть', 'основание выезда', 'пожарная техника', 'номер',
                          'спидометр при выезде',
                          'спидометр при возвращении', 'фактический расход', 'нормативный расчет']],
                page_size=18,
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
                    }])], className='second_columns'),

        html.Div([

            dcc.Graph(id='my_graph', className='graph'),
            html.Div('Фактический расход топлива: ', id='current_expence', className='graph'),
            dcc.Graph(id='my_graph3', className='graph'),
            dcc.Graph(id='my_graph4', className='graph')], className='third_columns'),

    ], className='first_line'),

    html.Div([
        html.Div(id='placeholder', children=[]),
        dcc.Store(id="store", data=0),
        dcc.Interval(id='interval', interval=3000),
        dcc.Interval(id='interval1', interval=3000),

    ]),
])


@app.callback(
    [dash.dependencies.Output('values', 'options'),
     dash.dependencies.Output('fire_auto', 'options')],
    [
        dash.dependencies.Input('brigate', 'value'),

    ],
)
def update_output(brigate):
    list_department = [{'label': a, 'value': a} for a in suka[brigate]['brigate']]
    list_fire_auto = [{'label': a, 'value': a} for a in suka[brigate]['auto']]
    return list_department, list_fire_auto


@app.callback(
    dash.dependencies.Output('gov_number', 'options'),
    [dash.dependencies.Input('fire_auto', 'value'),
     dash.dependencies.Input('brigate', 'value')],
)
def update_output(fire_auto, brigate):
    list_gov_number = [{'label': a, 'value': a} for a in suka[brigate][fire_auto]]
    return list_gov_number


@app.callback(
    [dash.dependencies.Output('placeholder', 'children'),
     dash.dependencies.Output("store", "data")
     ],

    [dash.dependencies.Input('save_to_postgres', 'n_clicks'),
     dash.dependencies.Input("interval", "n_intervals")],

    [dash.dependencies.State('brigate', 'value'),
     dash.dependencies.State('values', 'value'),
     dash.dependencies.State('store', 'data'),
     dash.dependencies.State('calendar', 'date'),
     dash.dependencies.State('time_out', 'value'),
     dash.dependencies.State('gov_number', 'value'),
     dash.dependencies.State('fire_auto', 'value'),
     dash.dependencies.State('speedometr_start', 'value'),
     dash.dependencies.State('speedometr_end', 'value'),
     dash.dependencies.State('work_pump', 'value'),
     dash.dependencies.State('without_pump', 'value'),
     dash.dependencies.State('department4', 'value'),
     dash.dependencies.State('date_return', 'date'),
     dash.dependencies.State('time_return', 'value'),
     dash.dependencies.State('reason_leaving', 'value'),
     ], prevent_initial_call=True)
def update_output(n_clicks, n_intervals, brigate, values, s, calendar, time_out, fire_auto, gov_number,
                  speedometr_start, speedometr_end, work_pump, without_pump, department4, date_return, time_return,
                  reason_leaving):
    output = html.Pre("Спасибо, Ваши данные сохранены в PostgreSQL",
                      style={'color': 'green', 'font-weight': 'bold', 'font-size': 'large'})
    # no_output = html.Pre("Не сохранены", style={'margin': "0px"})
    no_output = html.Pre("Не сохранены", style={'color': 'red', 'font-weight': 'bold', 'font-size': 'large'})

    input_triggered = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    if input_triggered == 'save_to_postgres':
        s = 4
        with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) as conn:
            cur = conn.cursor()
            cur.execute(
                f"INSERT INTO productlist VALUES ('{brigate}', '{values}', '{calendar}' , '{time_out}', "
                f"'{gov_number}', '{fire_auto}', '{speedometr_start}', '{speedometr_end}', '{work_pump}', "
                f"'{without_pump}', '{department4}', '{date_return}', '{time_return}', '{reason_leaving}')")

        return output, s

    elif input_triggered == 'interval' and s > 0:
        s = s - 1
        if s > 0:
            return output, s
        else:
            return no_output, s

    elif s == 0:
        return no_output, s


@app.callback(
    [dash.dependencies.Output('my_graph', 'figure'),
     dash.dependencies.Output('the_table', 'data'),
     dash.dependencies.Output("current_expence", "children")],
    [dash.dependencies.Input('brigate', 'value'),
     dash.dependencies.Input('values', 'value'),
     dash.dependencies.Input("interval1", "n_intervals"),
     dash.dependencies.Input('brigate2', 'value'), ],
    [dash.dependencies.State('the_table', 'data'),
     ],
    prevent_initial_call=True)
def display_graph(department, values, interval1, department_dropdown, data):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM total_consumption_join_main4;")
        data = cur.fetchall()

        cur.execute("SET timezone = 'Asia/Sakhalin';")

        cur.execute("SELECT * FROM date_current1;")

        current_expence = cur.fetchone()

        cur.execute("SELECT * FROM current_expence;")

        current_expence_department = cur.fetchall()

        current_expence_department = pd.DataFrame(current_expence_department, columns=['отряд', 'фактический расход'])

        def current_expence_filter():
            if department_dropdown != None:
                current_expence = current_expence_department[(current_expence_department['отряд'] \
                                                              == department_dropdown)]['фактический расход']
                return html.H1(current_expence)
            else:
                current_expence1 = current_expence_department['фактический расход'].sum()
                return current_expence1

        pg = pd.DataFrame(data, columns=['дата', 'отряд', 'часть', 'основание выезда', 'пожарная техника', 'номер',
                                         'спидометр при выезде',
                                         'спидометр при возвращении', 'фактический расход', 'нормативный расчет'])
        pg.loc[:, 'фактический расход'] = pd.to_numeric(pg['фактический расход'], errors='coerce')

        table_data = pg.copy()
        table_data1 = pg.copy()

        def table_data_filter():
            if department_dropdown != None:
                filtered_df = table_data[(table_data['отряд'] == department_dropdown)][
                    ['дата', 'отряд', 'часть', 'основание выезда', 'пожарная техника', 'номер', 'спидометр при выезде',
                     'спидометр при возвращении', 'фактический расход', 'нормативный расчет']]
                return filtered_df
            else:
                return table_data1

        pg = round(pg.groupby(['отряд'], as_index=False)['фактический расход'].sum(), 2)

        fig = px.bar(pg, x='отряд', y='фактический расход')

        dff = pg.copy()
        dff.loc[:, 'фактический расход'] = pd.to_numeric(dff['фактический расход'], errors='coerce')

        dff = round(dff.groupby(['отряд'], as_index=False)['фактический расход'].sum(), 2)

    return fig, table_data_filter().to_dict('records'), current_expence_filter()


if __name__ == '__main__':
    app.run_server(debug=True)
