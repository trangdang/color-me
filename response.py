import cluster
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get-colors', methods=['POST'])
def return_colors():
    json_content = request.json['content']
    color_output = cluster.process(json_content)
    return jsonify(colorlist=color_output)
        
if __name__ == '__main__':
    app.run()
