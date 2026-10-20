from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


LEMONADES = [
    {
        "id": 1,
        "name": "Классический",
        "color": "#FFD700",
        "description": "Лимон, вода, сахар. Идеален в жару.",
        "price": 150
    },
    {
        "id": 2,
        "name": "Мятный",
        "color": "#98FF98",
        "description": "Свежий лимон с добавлением мяты.",
        "price": 180
    },
    {
        "id": 3,
        "name": "Клубничный",
        "color": "#FFB6C1",
        "description": "Сладкий, розовый и очень вкусный.",
        "price": 200
    },
    {
        "id": 4,
        "name": "Лавандовый",
        "color": "#E6E6FA",
        "description": "Нежный вкус с цветочным ароматом.",
        "price": 220
    }
]

@app.route('/api/lemonades')
def get_lemonades():

    return jsonify(LEMONADES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)