## Decorators in Flask

**Estimated time needed: 10 minutes**

### Objectives
After reading this page, you will be able to:
- Understand what decorators are.
- Recognize the two kinds of decorators you come across in a Python application.
- Know when and how to use decorators.

### What are Decorators?
Decorators help in annotating methods and indicate what a particular method is meant for. They are different from comments because they are used by the interpreter while running the code.

### Method Decorators
Method decorators can be used to modify the output of functions without altering their core logic. For example, if you want all output to be in JSON format, you can use a decorator to handle this, avoiding redundancy in your code.

```python
def jsonify_decorator(function):
    def modifyOutput():
        return {"output": function()}
    return modifyOutput

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1) + int(num2)

print(hello())
print(add())
```

**Explanation:**
- `jsonify_decorator` is the decorator method that wraps the output of `hello()` and `add()` functions.
- The output of these methods will be modified by the `jsonify_decorator`.

### Route Decorators
Route decorators in Flask are used to assign URLs to functions, creating endpoints for your web application.

**Basic Route Example:**

```python
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"
```

**Explanation:**
- `@app.route("/")` assigns the root URL to the `home()` function.
- Multiple routes can be handled by stacking additional route decorators.

**Dynamic Route Example:**

```python
@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for " + userid
```

**Explanation:**
- `@app.route("/userdetails/<userid>")` defines a dynamic route that captures `userid` from the URL and passes it to the `getUserDetails()` function.

Congratulations! You have just learned about decorators in Python. Go ahead and use them in your code.