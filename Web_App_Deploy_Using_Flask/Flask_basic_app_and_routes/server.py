from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/no_content')
def no_content():
    """ Returns 'No content found' with a status code of 204
    Returns:
        json : message : No content found
        status code : 204
    """
    return ({"message" : "No content found"}, 204)


@app.route('/exp')
def index_explicit():
    """ Returns 'Hello, World!' with a status code of 200
    Returns:
        string : Hello, World!
        status code : 200
    """
    res = make_response({"message" : "Hello, World!"})
    res.status_code = 200
    return res

@app.route('/exp2')
def index_explicit2():
    """ Returns 'Hello, World!' with a status code of 200
    Returns:
        string : Hello, World!
        status code : 200
    """
    return ({"message" : "Hello, World!"}, 200)