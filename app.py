from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Path to the JSON file
json_file = 'config.json'


def load_json():
    with open(json_file, 'r') as file:
        return json.load(file)


def save_json(data):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


@app.route('/')
def index():
    json_data = load_json()
    return render_template('index.html', json_data=json_data)


@app.route('/json', methods=['GET'])
def get_json():
    json_data = load_json()
    return jsonify(json_data)


@app.route('/json', methods=['POST'])
def edit_json():
    new_data = request.get_json()
    # json_data = load_json()
    # json_data.update(new_data)
    save_json(new_data)
    return jsonify(new_data)

@app.route('/add', methods=['POST'])
def add_json():
    new_data = request.get_json()
    json_data = load_json()
    json_data.append(new_data)
    save_json(json_data)
    return jsonify(json_data)

@app.route('/status', methods=['GET'])
def get_status():
    json_data = load_json()
    statuses = []
    for data in json_data:
        data['status'] =  check_config_status(data)
        statuses.append(data)
    return jsonify(statuses)

import cv2
def check_config_status(json_data):
    try:
      cap = cv2.VideoCapture(json_data["rtsp_video"])
      ret, frame = cap.read()
      if ret:
        return 'Working'
      return 'Not Working'
    except Exception as e:
      print(e)
      return 'Not Working'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
