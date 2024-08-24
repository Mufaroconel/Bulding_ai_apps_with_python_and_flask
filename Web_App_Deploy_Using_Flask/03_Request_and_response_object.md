
### **Request and Response Objects in Flask**

**Objective:**
After completing this module, you will be able to:
- Understand and explain the Flask Request Object.
- Understand and explain the Flask Response Object.

**Understanding Flask Routes:**
1. **Defining Routes:**
   - Use the `@app.route` decorator to define paths in your Flask application.
   - By default, the `@app.route` decorator handles `GET` requests.
   - To allow other HTTP methods (e.g., `POST`), pass them as a list in the `methods` argument.

2. **Customizing Routes:**
   - Example: A `/health` route that responds to both `GET` and `POST` methods.
   - Output varies based on the HTTP method used.

**Exploring the Flask Request Object:**
1. **Attributes of the Request Object:**
   - **Host and Port:** Tuple containing the server address.
   - **Headers:** Information about the request headers.
   - **URL:** The requested resource URL.
   - **access_route:** Lists IP addresses for requests forwarded multiple times.
   - **full_path:** Complete path including any query strings.
   - **is_secure:** Boolean indicating if the request is over HTTPS.
   - **is_json:** Boolean indicating if the request contains JSON data.
   - **Cookies:** Dictionary of cookies sent with the request.

2. **Common Request Headers:**
   - **Cache-Control:** Instructions for caching in browsers.
   - **Accept:** Content types understood by the client.
   - **Accept-Encoding:** Types of encoding accepted by the client.
   - **User-Agent:** Identifies the client (e.g., browser, OS).
   - **Accept-Language:** Language and locale preferences.
   - **Host:** Host and port number of the requested server.

3. **Accessing Data from the Request Object:**
   - Use `get_data()` to retrieve data as bytes (you will need to parse this data).
   - Use `get_json()` to parse POST request data as JSON.
   - Use specific attributes (`args`, `json`, `files`, `form`, `values`) to get exact data types without additional parsing.

4. **Extracting Specific Values:**
   - Data structures like `MultiDict`, `ImmutableMultiDict`, or `CombinedMultiDict` are used to hold data in the request object.
   - Extract values using indexing or the `get()` method, with the latter providing safer error handling.

**Exploring the Flask Response Object:**
1. **Common Response Attributes:**
   - **status_code:** Indicates the success or failure of the request.
   - **headers:** Information about the response headers.
   - **content_type:** Media type of the response.
   - **content_length:** Size of the response message body.
   - **content_encoding:** Encoding applied to the response.
   - **mime-type:** Media type of the response.
   - **expires:** Date/time after which the response is considered expired.

2. **Standard Response Methods:**
   - **set_cookie():** Sets a browser cookie on the client.
   - **delete_cookie():** Deletes a cookie on the client.
   - **make_response():** Creates a custom response.
   - **redirect():** Returns a `302` status code and redirects the client to another URL.
   - **abort():** Returns a response with an error condition.

**Summary:**
- Flask provides a `Request` and a `Response` object for each client call.
- You can access request headers, query parameters, and body content using the `Request` object.
- You can customize response attributes and status codes before sending them back to the client using the `Response` object.

---