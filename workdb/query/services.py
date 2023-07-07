import pyodbc
from typing import Union


def execute_query(query: str) -> Union[dict, tuple]:
    """
    1. Подключаемся к базе
    2. Формируем словарь для таблицы шаблона (query/index.html). В случае ошибки - возвращаем ошибку.
        {
            field1: [value1, value2 ...],
            ...
        }
    """
    with pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};'   # Указываем драйвер для подключения к серверу БД
            'SERVER={OIASUP-SHAMION7};'                 # Устройство где установлен сервер БД
            'DATABASE=AdventureWorks;'                  # Указываем БД
            'TRUSTED_CONNECTION=yes;') as connect:      # Устанавливаем доверен. соединение без логин/пароль
        cursor = connect.cursor()

    data = dict()
    try:
        for row in cursor.execute(query).fetchall():
            for pos, col in enumerate(row.cursor_description):
                column = col[0]
                data.setdefault(column, [])
                data.get(column).append(row[pos])
    except (pyodbc.ProgrammingError, pyodbc.Error) as e:
        data = e.args

    return data























