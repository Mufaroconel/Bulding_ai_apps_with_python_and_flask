from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/no_content')
def no_method():
    """"
    return 'No content found' with a status code of 204

    returns:
        string : No content found
        status code : 204
    """
    return jsonify{}