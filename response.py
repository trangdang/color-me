import cluster
from flask import Flask, request, jsonify, url_for, redirect
app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('static', filename='index.html'))

@app.route('/get-colors', methods=['POST'])
def return_colors():
    json_content = request.json['content']
    color_output = cluster.process(json_content, 8)
    return jsonify(colorlist=color_output)
        
if __name__ == '__main__':
    app.debug = True
    app.run()
