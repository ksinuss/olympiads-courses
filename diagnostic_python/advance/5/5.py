import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def form_output(events: list):
    events_ = sorted(events, key=lambda x: (x[0], x[1]))
    spiral_dict = {}
    for event in events_:
        area = event[2]
        event_list = [
            event[0],
            event[1]
        ]
        if area not in spiral_dict:
            spiral_dict[area] = [event_list]
        else:
            spiral_dict[area].append(event_list)
    return spiral_dict

def get_data_evolution(file_name='evolution.txt'):
    with open(file_name) as file:
        db_file = file.readline().strip()
        max_remoteness = int(file.readline())
    return db_file, max_remoteness

def get_dict():
    db_file, max_remoteness = get_data_evolution()
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            request = f'''
                SELECT centuries_ago, event, area
                FROM events
                WHERE centuries_ago <= {max_remoteness}
            '''
            cursor.execute(request)
            events = cursor.fetchall()
            spiral_dict = form_output(events)
            return spiral_dict
    except Exception:
        return {}

@app.route('/spiral', methods=['GET'])
def get_spiral():
    spiral_dict = get_dict()
    return jsonify(spiral_dict)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
