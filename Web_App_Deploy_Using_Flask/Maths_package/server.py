from flask import Flask, render_template, request
from Maths_package.mathematics import summation, subtraction, multiplication

app = Flask(__name__)

@app.route('/')
def render_index_page():
    return render_template('index.html')

# @app.route('/sum')
# def sum():
#     num1 = float(request.args.get('num1'))
#     num2 = float(request.args.get('num2'))
#     result = summation(num1, num2)
#     return str(result)

# @app.route('/sub')
# def sub():
#     num1 = float(request.args.get('num1'))
#     num2 = float(request.args.get('num2'))
#     result = subtraction(num1, num2)
#     result = str(result)
#     return result

# @app.route('/mul')
# def mul():
#     num1 = float(request.args.get('num1'))
#     num2 = float(request.args.get('num2'))
#     result = multiplication(num1, num2)
#     result = str(result)
#     return result