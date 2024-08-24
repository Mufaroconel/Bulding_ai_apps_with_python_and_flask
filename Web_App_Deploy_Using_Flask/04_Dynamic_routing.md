# Dynamic Routes

## Key Learning Outcomes
- **Call an External API in Flask**: Learn how to use the `requests` library to interact with external APIs.
- **Pass Parameters to Routes in Flask**: Understand how to create dynamic routes that accept parameters.

## Example: Calling an External API
1. **Import Necessary Modules**: 
   - Import `flask` and `requests`.
   
2. **Define a Route**: 
   - Use the `requests` library to call the OpenLibrary API and search for information about an author.
   
3. **Process and Return the Response**: 
   - Check the API's response status code:
     - **200**: Return the JSON data to the client.
     - **404**: Return a message, "Something went wrong."
     - **Other**: Return a status of 500 with the message "Server error."

## Example: Dynamic Routes with Parameters
1. **Dynamic Route Creation**: 
   - Create a route that includes a dynamic part of the URL, such as an ISBN number.
   - Pass the dynamic part (ISBN) to the OpenLibrary API and return the results to the client.

2. **Parameter Type Validation**: 
   - Set specific types for route parameters (e.g., `string`, `int`, `float`, `path`, `UUID`).
   - Use parameter types to validate incoming requests.

## Example: UUID Parameter
- **Create a Route with UUID**: 
  - Define an endpoint that expects a UUID.
  - Check if the UUID exists, and return a success message if found. Otherwise, return an appropriate error message.

## Summary
- **Request Object Parsing**: Extract query parameters, body, and other arguments.
- **Response Object Customization**: Set status codes and headers before sending a response.
- **Dynamic Routes**: Create RESTful endpoints using dynamic route parameters.
