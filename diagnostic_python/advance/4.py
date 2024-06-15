import csv
import sqlite3

def get_csv_file(output: list):
    field_names = [
        'expedition_id', 
        'designation', 
        'target', 
        'ship', 
        'engine',
        'year'
    ]   
    with open('useful.csv', 'w') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(output)

def form_output(filler: dict):
    print(filler)
    # output_ = output
    # for heading in elements:
    #     output_[heading] = elements[heading]
    #     print(output_)
    #     if all(output[heading] for heading in output_):
    #         OUTPUT.append(output_)
    #     return output

def choosing_next_step(name_table, correct_id: list, step_number):
    # print(name_table, correct_id)
    next_step = steps[NAME_TABLE][step_number]
    value = map(str, MARKS[next_step['value']])
    filler = []
    if name_table == 'engines':
        for id in correct_id:
            engine_id = id[0]
            MARKS['engine_id'].add(engine_id)
            filler.append((engine_id, {'engine': id[1]}))
    if name_table == 'ships':
        for id in correct_id:
            MARKS['ship_id'].add(id[0])
            MARKS['engine_id'].add(id[2])
            filler.append(({'ship': id[1]}))
    if name_table == 'expeditions':
        for id in correct_id:
            ship_id = id[4]
            MARKS['ship_id'].add(ship_id)
            filler.append((
                ship_id,
                {
                    'expedition_id': id[0],
                    'designation': id[1],
                    'target': id[2],
                    'year': id[3]
                }
            ))
    form_output(filler)
    name_table = next_step['name_table']
    name_column = next_step['name_column']
    # print(name_table, name_column, value)
    take_correct_id(name_table, name_column, '=', value, step_number+1)

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
            # print(correct_id)
            choosing_next_step(name_table, correct_id, step_number)
            # return correct_id
    except Exception as e:
        print(e)
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
OUTPUT = []

take_correct_id(NAME_TABLE, name_column, '<', [max_value])

print(OUTPUT)
# get_csv_file(OUTPUT)
