from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/spiral', methods=['GET'])
def get_spiral():
    spiral_dict = {
        "shape": "spiral",
        "color": "blue",
        "size": "large"
    }
    return jsonify(spiral_dict)

if __name__ == '__main__':
    app.run(debug=True)
