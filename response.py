import cluster
from flask import Flask, request, jsonify
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def main():
    return 

@app.route('/get-colors', methods=['OPTIONS'])
def return_colors():
    print request
    print request.args
    print "----------------"

    json_content = request.json['content']
    print "------------json content"
    print json_content

    color_output = cluster.process(json_content)
    print "-------------color output"
    print color_output

    return jsonify(colorlist=color_output)
        
if __name__ == '__main__':
    app.debug = True
    app.run()
