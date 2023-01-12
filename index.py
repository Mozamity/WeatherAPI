from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return 'Hello Moozakeer!'






@app.route('/guide', methods=["POST"])
def add_guide():
    title = request.json['title']
    content = request.json['content']

    
    guide = 'Sunny'

    return jsonify(content)

if __name__ == '__main__':
    app.run()
