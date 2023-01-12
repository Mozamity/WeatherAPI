
from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return 'Hello World!'






@app.route('/weather', methods=["POST"])
def add_guide():
    LDR = request.json['LDR']
    rain = request.json['rain']
    wind = request.json['wind']
    
    if rain > 0 and wind > 50 and LDR == 1:
    	weather = 'Rainy and Windy'

    if rain == 0 and wind > 50 and LDR == 0:
    	weather = 'Sunny and Windy'

    if rain == 0 and wind < 50 and LDR == 0:
    	weather = 'Sunny'

    if rain > 0 and wind < 50 and LDR == 1:
    	weather = 'Rainy'

    if rain == 0 and wind < 50 and LDR == 1:
    	weather = 'cloudy'

    if rain == 0 and wind > 50 and LDR == 1:
    	weather = 'cloudy and windy'

    

    
    guide = 'Sunny'

    return jsonify(weather)

if __name__ == '__main__':
    app.run()
