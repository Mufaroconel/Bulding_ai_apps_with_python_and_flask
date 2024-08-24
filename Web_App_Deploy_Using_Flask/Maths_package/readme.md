# Hands-on Lab: Building and Deploying a Web App using Flask

## Introduction

In this lab, we create a basic application of mathematical functions and deploy it over a web interface using Flask. The purpose is to connect all the pieces of knowledge gained in the course till now, and see the application development and deployment steps in action.

**Estimated time needed:** 30 minutes

## Objectives

In this assignment you will:

1. **Task 1:** Create the mathematical functions.
2. **Task 2:** Package the functions and test the package.
3. **Task 3:** Web Deployment of the application package using Flask.

## Task 1: Write the Mathematical Functions

In this task, you are required to write a script that has functions to add, subtract, and multiply two values. Let's call this script `mathematics.py`.

Follow the steps for this task:

1. **Open a terminal window** by using the menu in the editor: `Terminal > New Terminal`.

2. **Go to the project home directory.**

    ```bash
    cd /home/project
    ```

3. **Run the following command** to Git clone the project directory from the clone URL you had copied in the prework lab.

    ```bash
    git clone https://github.com/ibm-developer-skills-network/hjbsk-build_deploy_app_flask
    ```

4. **Change to the `practice_project` folder.**

    ```bash
    cd /home/project/hjbsk-build_deploy_app_flask
    ```

5. **Create a folder named `Maths` and change to that directory.**

    ```bash
    mkdir Maths
    cd Maths
    ```

6. **In the explorer, go to the `Maths` directory and create a new file called `mathematics.py`.**

7. **Add the following functions to `mathematics.py`:**

    - **Summation Function**

        ```python
        def summation(a, b):
            result = a + b
            return result
        ```

    - **Subtraction Function**

        ```python
        def subtraction(a, b):
            result = a - b
            return result
        ```

    - **Multiplication Function**

        ```python
        def multiplication(a, b):
            result = a * b
            return result
        ```

## Task 2: Package the Functions

1. **Create an `__init__.py` file** in the `Maths` directory.

    - Import the `mathematics.py` file into the `__init__.py` file.

        ```python
        from . import mathematics
        ```

2. **Import the `Maths` package in `server.py`.**

    ```python
    from Maths.mathematics import summation, subtraction, multiplication
    ```

3. **In `server.py`, for the endpoint `/`, implement a method that renders `index.html`.**

    ```python
    @app.route("/")
    def render_index_page():
        return render_template('index.html')
    ```

4. **In `server.py`, for the endpoint `/sum`, implement a method that uses the `summation` function.**

    - The function should take the arguments `num1` and `num2` as float input through the request parameters and return a string output.

    ```python
    @app.route("/sum")
    def sum():
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = summation(num1, num2)
        return str(result)
    ```

5. **In `server.py`, for the endpoint `/sub`, implement a method that uses the `subtraction` function.**

    - The function should take the arguments `num1` and `num2` as float input through the request parameters and return a string output.

    ```python
    @app.route("/sub")
    def subtract():
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = subtraction(num1, num2)
        return str(result)
    ```

6. **In `server.py`, for the endpoint `/mul`, implement a method that uses the `multiplication` function.**

    - The function should take the arguments `num1` and `num2` as float input through the request parameters and return a string output.

    ```python
    @app.route("/mul")
    def multiply():
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = multiplication(num1, num2)
        return str(result)
    ```
## Task 3: Web Deployment of the Application Package Using Flask

1. **Change the current directory** on the terminal to the `hjbsk-build_deploy_app_flask` directory and run the server:

    ```bash
    cd /home/project/hjbsk-build_deploy_app_flask && python3.11 server.py
    ```

    - The server will start up on port 8080.

2. **Open the Skills Network Toolbox**:

    - Click the "Skills Network" button on the left.
    - Click "Other" and then "Launch Application."
    - Enter the port number (8080) and click the "Launch" button.

3. **A new browser window** will open with the index page.

4. **Test your application** to ensure it produces the desired outputs. Some example outputs should be verified to confirm proper functionality.
