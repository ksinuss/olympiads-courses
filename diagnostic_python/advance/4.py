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

def form_output(elements: dict, filler: dict):
    output_ = output
    for heading in elements:
        output_[heading] = elements[heading]
        print(output_)
        if all(output[heading] for heading in output_):
            OUTPUT.append(output_)
        return output

def choosing_next_step(name_table, sign, correct_id: list):
    print(name_table, sign, correct_id)
    

    # if name_table == 'engines':
    #     if sign == '<':
    #         for id in correct_id:
    #             engine_id = id[0]
    #             engine = id[1]
    #             output_ = form_output({'engine': engine})
    #             # print(output_)
    #             take_correct_id('ships', 'engine_id', '=', engine_id, output_)
    #     if sign == '=':
    #         pass
    # if name_table == 'ships':
    #     if sign == '<':
    #         pass
    #     if sign == '=':
    #         for id in correct_id:
    #             ship_id = id[0]
    #             ship = id[1]
    #             output_ = form_output({'ship': ship}, output)
    #             print(output_)
    #             take_correct_id('expeditions', 'ship_id', '=', ship_id, output_)
    # if name_table == 'expeditions':
    #     if sign == '<':
    #         pass
    #     if sign == '=':
    #         for id in correct_id:
    #             form_output(
    #                 {
    #                     'expedition_id': id[0],
    #                     'designation': id[1],
    #                     'target': id[2],
    #                     'year': id[3]
    #                 },
    #                 output
    #             )

def take_correct_id(name_table, name_column, sign, value: list):
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
            print(correct_id)
            choosing_next_step(name_table, sign, correct_id)
            # return correct_id
    except Exception as e:
        print(e)
        return None

# INPUT
# name_file = input()
# name_table, name_column = input().split()
# max_value = input()
NAME_FILE = 'expeditions.db'
name_table, name_column = 'engines', 'engine'
max_value = 'electric'

steps = {
    'expeditions': {
        '<': {
            'name_table': 'ships',
            'name_column': 'id',
            'sign': '='
        },
        '=': {
            'name_table': 'engines',
            'name_column': 'id',
            'sign': '='
        }
    },
    'ships': {
        '<': {
            'name_table': 'expeditions',
            'name_column': 'ship_id',
            'sign': '='
        },
        '=': {
            'name_table': 'expeditions',
            'name_column': 'ship_id',
            'sign': '='
        }
    },
    'engines': {
        '<': {
            'name_table': 'ships',
            'name_column': 'engine_id',
            'sign': '='
        },
        '=': {
            'name_table': 'ships',
            'name_column': 'id',
            'sign': '=',
            'value': 4
        }
    }
}
OUTPUT = []

take_correct_id(name_table, name_column, '<', [max_value])

print(OUTPUT)
# get_csv_file(OUTPUT)
