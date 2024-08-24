# Error Handling in Flask

## Key Takeaways
- **Understanding HTTP Status Codes**: HTTP responses include three-digit codes that indicate the status of the request.
  - **100-199**: Informational - Request received.
  - **200-299**: Success - Request was successful.
  - **300-399**: Redirection - Further action needed.
  - **400-499**: Client Error - Error in the request.
  - **500-599**: Server Error - Server failed to fulfill the request.

- **Flask Default Behavior**:
  - Flask automatically returns a `200 OK` status for successful requests.
  - Using the `jsonify` method also defaults to a `200 OK` status.

- **Customizing Response Status Codes**:
  - Flask allows you to specify status codes with responses using tuples.
  - Example: `make_response` can be used to explicitly set status codes.

## Common HTTP Status Codes in Flask
- **200 OK**: Request successful.
- **201 Created**: Resource successfully created.
- **204 No Content**: Request successful, no content to return.
- **400 Bad Request**: Invalid request parameters.
- **401 Unauthorized**: Missing or invalid credentials.
- **403 Forbidden**: Insufficient client credentials.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: Server encountered an error.

## Example of Error Handling in Flask
- **Handling Missing Parameters**: Return `422 Unprocessable Entity` if parameters are missing.
- **Resource Not Found**: Return `404 Not Found` if the requested resource doesn't exist.
- **Application-Level Error Handling**:
  - Define custom error handlers for common errors like `404` and `500`.

## Conclusion
- Always return appropriate status codes to indicate the outcome of API requests.
- Use Flask's built-in methods to handle errors effectively at both the route and application levels.
