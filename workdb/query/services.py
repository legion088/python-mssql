import pyodbc
from typing import Union


def execute_query(query: str) -> Union[dict, tuple]:
    with pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};'
            'SERVER={lenovo};'
            'DATABASE=students;'
            'TRUSTED_CONNECTION=yes;') as connect:
        cursor = connect.cursor()

    command = ['insert', 'update', 'delete']
    data = dict()

    if any(com in query.lower() for com in command):
        cursor.execute(query)
        cursor.commit()
        return data

    try:
        for row in cursor.execute(query).fetchall():
            for pos, col in enumerate(row.cursor_description):
                column = col[0]
                data.setdefault(column, [])
                data.get(column).append(row[pos])
    except (pyodbc.ProgrammingError, pyodbc.Error) as e:
        data = e.args
    return data

