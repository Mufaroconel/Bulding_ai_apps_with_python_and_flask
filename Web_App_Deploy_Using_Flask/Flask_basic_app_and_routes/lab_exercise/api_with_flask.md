## Exercise: Setting Custom HTTP Response Status Codes in Flask

### Step 1: Set Response Status Code

In the last part, you saw Flask automatically send an HTTP 200 OK successful response when you sent back a message. However, you can also set the return status explicitly. Recall that there are two ways to do this:

1. Send a tuple back with the message.
2. Use the `make_response()` method to create a custom response and set the status.

---

### Your Tasks

1. **Send a custom HTTP code back with a tuple:**

    - Reuse the `server.py` file you worked on in the last part.
    - Create a new method named `no_content` with the `@app.route` decorator and URL of `/no_content`.
    - The method does not have any arguments. Return a tuple with the JSON message `"No content found"` and the status code `204`.

---

**Hint:**

You can use the following skeleton code as a start:

```python
@app.route("/no_content")
def no_content():
    """Return 'No content found' with a status of 204
    Returns:
        string: No content found
        status code: 204
    """
    return ({"message": "No content found"}, 204)
```

You can test the endpoint with the following CURL command:

```bash
curl -X GET -i -w '\n' localhost:5000/no_content
```

You should see an output similar to the following. Note the status of `204` and the `Content-Type` of `application/json`. Even though you returned a JSON message, it is not sent back to the client with a `204` status code. By default, nothing is returned.

```plaintext
HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 19:49:18 GMT
Content-Type: application/json
Connection: close
```

---

2. **Send a custom HTTP code back with the `make_response()` method:**

    - Create a second method named `index_explicit` with the `@app.route` decorator and a URL of `/exp`.
    - The method does not have any arguments. Use the `make_response()` method to create a new response. Set the status to `200`.

---

**Hint:**

1. Import the `Flask` class from the `flask` module.
2. Import the `make_response` method from the `flask` module.

```python
@app.route("/exp")
def index_explicit():
    """Return 'Hello World' message with a status code of 200
    Returns:
        string: Hello World
        status code: 200
    """
    resp = make_response({"message": "Hello World"})
    resp.status_code = 200
    return resp
```

You can test the endpoint with the following CURL command:

```bash
curl -X GET -i -w '\n' localhost:5000/exp
```

You should see an output similar to the one given below. Note the status of `200`, `Content-Type` of `application/json`, and JSON output of `{"message": "Hello World"}`:

```plaintext
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 19:55:46 GMT
Content-Type: application/json
Content-Length: 31
Connection: close
{
  "message": "Hello World"
}
```

---

### Solution

Double-check that your work matches the following solution.

```python
from flask import Flask, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "Hello World"

# Define a route for the "/no_content" URL
@app.route("/no_content")
def no_content():
    """Return 'No content found' with a status of 204.
    Returns:
        tuple: A tuple containing a dictionary and a status code.
    """
    # Create a dictionary with a message and return it with a 204 No Content status code
    return ({"message": "No content found"}, 204)

# Define a route for the "/exp" URL
@app.route("/exp")
def index_explicit():
    """Return 'Hello World' message with a status code of 200.
    Returns:
        response: A response object containing the message and status code 200.
    """
    # Create a response object with the message "Hello World"
    resp = make_response({"message": "Hello World"})
    # Set the status code of the response to 200
    resp.status_code = 200
    # Return the response object
    return resp
```
