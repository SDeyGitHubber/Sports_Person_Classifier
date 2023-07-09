from flask import Flask, request, jsonify
import util

app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }
        return '', 200, headers
    else:
        headers = {
            'Access-Control-Allow-Origin': '*'
        }
        request.headers = headers

@app.route('/upload', methods=['POST'])
def upload():
    # Your file upload code here
    return jsonify({'success': True})


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000,debug=True)