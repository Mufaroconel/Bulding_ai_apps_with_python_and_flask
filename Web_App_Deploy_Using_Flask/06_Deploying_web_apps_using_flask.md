## Deploying Web Apps using Flask

### Overview
- **Flask** is a micro framework for creating web applications with Python.
- **CRUD Operations**: Flask supports Create, Read, Update, and Delete requests.

### CRUD Operations
- **Post and Put Requests**:
  - **Post**: Creates new data on every request.
  - **Put**: Creates data on the first request and updates it in subsequent requests.
- **Get Request**: Reads data from the server.
- **Update and Delete Requests**: Used to update or delete existing data.

### Creating a Web Application with Flask

#### Steps:

1. **Install Flask**
   ```bash
   pip install Flask
   ```

2. **Import Flask Module**
   ```python
   from flask import Flask
   ```

3. **Create Flask Application**
   ```python
   app = Flask("My first Application")
   ```

4. **Define Routes and Methods**
   - **Root Route**
     ```python
     @app.route('/')
     def hello():
         return 'Hello World!'
     ```

5. **Run the Application**
   ```python
   if __name__ == "__main__":
       app.run(debug=True)
   ```

6. **Check Endpoints**
   - Open a browser and navigate to `http://127.0.0.1:5000/` to see "Hello World".

### Working with Templates

- **Static and Dynamic Templates**:
  - **Static**: Served as-is from the `static` directory.
  - **Dynamic**: Rendered based on request parameters, using the `templates` directory.

#### Example Flask Application:

1. **Import Required Modules**
   ```python
   from flask import Flask, render_template, request
   ```

2. **Instantiate Flask Application**
   ```python
   app = Flask("My first Application")
   ```

3. **Define Endpoints**
   - **Static Page**
     ```python
     @app.route('/sample')
     def getSampleHtml():
         return render_template('sample.html')
     ```
   - **Dynamic Page (URL Parameter)**
     ```python
     @app.route('/user/<username>', methods=['GET'])
     def show_user_profile(username):
         return f'User {username}'
     ```
   - **Dynamic Page (Request Parameter)**
     ```python
     @app.route('/user')
     def show_user_profile():
         username = request.args.get('username')
         return f'User {username}'
     ```

### Summary
- **Flask** is used for creating web applications and supports CRUD operations.
- Install Flask using Pip, create and run a Flask application, and handle static and dynamic templates.

---