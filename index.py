
from flask import Flask, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return 'Hello World!'






@app.route('/guide', methods=["POST"])
def add_guide():
    speed = request.json['speed']
    gyrosx = request.json['gyrosx']
    gyrosy = request.json['gyrosy']
    magnitude = request.json['magnitude']



    modelQA = pickle.load(open('ML/Decision-tree.pkl','rb'))
    arr = np.array([[speed, gyrosx, gyrosy, magnitude]])
    mlouptput = modelQA.predict(arr)

    if 'ok' in mlouptput:
        #OutputGB = 0
        roadsurface = 'ok'
        
    if 'hump' in mlouptput:
    #     #OutputGB = 2
        roadsurface = 'hump'

    if 'Pothole' in mlouptput:
    #     #OutputGB = 1
        roadsurface = 'Pothole'

    
    guide = 'Sunny'

    return jsonify(roadsurface)

if __name__ == '__main__':
    app.run()
