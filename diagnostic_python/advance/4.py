import csv
import sqlite3

def get_csv_file(output: list):
    output = sorted(output, key=lambda x: (x['year'], x['designation']))
    field_names = output[0].keys()  
    with open('useful.csv', 'w', encoding='utf8', newline='') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(output)

def form_output(output: list):
    output_ = []
    for expedition_id in output['expeditions'].keys():
        expedition = output['expeditions'][expedition_id]
        ship = output['ships'][expedition['ship_id']]
        engine = output['engines'][ship['engine_id']]
        expedition_ = {
            'expedition_id': expedition_id, 
            'designation': expedition['designation'], 
            'target': expedition['target'], 
            'ship': ship['ship'], 
            'engine': engine['engine'], 
            'year': expedition['year']
        }
        output_.append(expedition_)
    get_csv_file(output_)

def choosing_next_step(name_table: str, correct_id: list, step_number: int):
    if name_table == 'engines':
        for id in correct_id:
            engine_id = id[0]
            MARKS['engine_id'].add(engine_id)
            OUTPUT[name_table][engine_id] = {'engine': id[1]}
    if name_table == 'ships':
        for id in correct_id:
            ship_id = id[0]
            engine_id = id[2]
            MARKS['ship_id'].add(ship_id)
            MARKS['engine_id'].add(engine_id)
            OUTPUT[name_table][ship_id] = {'ship': id[1], 'engine_id': engine_id}
    if name_table == 'expeditions':
        for id in correct_id:
            ship_id = id[4]
            MARKS['ship_id'].add(ship_id)
            OUTPUT[name_table][id[0]] = {
                'designation': id[1],
                'target': id[2],
                'year': id[3],
                'ship_id': ship_id
            }
    if step_number + 1 <= len(steps[NAME_TABLE]):
        next_step = steps[NAME_TABLE][step_number]
        name_table = next_step['name_table']
        name_column = next_step['name_column']
        value = map(str, MARKS[next_step['value']])
        take_correct_id(name_table, name_column, '=', value, step_number + 1)

def take_correct_id(name_table, name_column, sign, value: list, step_number=0):
    try:
        with sqlite3.connect(NAME_FILE) as conn:
            cursor = conn.cursor()
            if sign == '<':
                value = value[0]
                request = f'''
                    SELECT *
                    FROM {name_table} 
                    WHERE {name_column} <= "{value}"
                '''
            if sign == '=':
                marks = ','.join(value)
                request = f'''
                    SELECT *
                    FROM {name_table}
                    WHERE {name_column} IN ({marks})
                '''
            cursor.execute(request)
            correct_id = cursor.fetchall() # fetchone - ТОЛЬКО 1 запись, fetchall - ВСЕ записи
            choosing_next_step(name_table, correct_id, step_number)
    except Exception as e:
        return None

# INPUT
# NAME_FILE = input()
# NAME_TABLE, name_column = input().split()
# max_value = input()
NAME_FILE = 'expeditions.db'
NAME_TABLE, name_column = 'engines', 'engine'
max_value = 'electric'

steps = {
    'expeditions': [
        {
            'name_table': 'ships',
            'name_column': 'id',
            'value': 'ship_id'
        },
        {
            'name_table': 'engines',
            'name_column': 'id',
            'value': 'engine_id'
        }
    ],
    'ships': [
        {
            'name_table': 'engines',
            'name_column': 'id',
            'value': 'engine_id'
        },
        {
            'name_table': 'expeditions',
            'name_column': 'ship_id',
            'value': 'ship_id'
        }
    ],
    'engines': [
        {
            'name_table': 'ships',
            'name_column': 'engine_id',
            'value': 'engine_id'
        },
        {
            'name_table': 'expeditions',
            'name_column': 'ship_id',
            'value': 'ship_id'
        }
    ]
}

MARKS = {
    'ship_id': set(),
    'engine_id': set()
}
OUTPUT = {
    'engines': {},
    'ships': {},
    'expeditions': {}
}

take_correct_id(NAME_TABLE, name_column, '<', [max_value])

form_output(OUTPUT)
