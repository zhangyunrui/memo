1. Terminologies
  - __Resource__ is an object or representation of something
  - __Collections__ are set of resources
  - __URL__ (Uniform Resource Locator) is a path through which a resource can be located and some actions can be performed on it
  
2. The paths should contain the __plural__ form of resources and the HTTP method should define the kind of __action__ to be performed on the resource

3. HTTP methods
  - `POST` is __non-idempotent__ which means multiple requests will have different effects
  - `PUT` is __idempotent__ which means multiple requests will have the same effects
  
4. HTTP response status codes
  - 2xx (Success category)
    - 200 Ok
    - 201 Created Using POST method, should always return 201 status code.
    - 204 No Content DELETE can be a good example of this.
  - 3xx (Redirection Category)
    - 304 Not Modified indicates that the client has the response already in its cache.
  - 4xx (Client Error Category)
    - 400 Bad Request
    - 401 Unauthorized
    - 403 Forbidden
    - 404 Not Found
    - 410 Gone
  - 5xx (Server Error Category)
    - 500 Internal Server Error
    - 503 Service Unavailable
    
5. If the request body or response type is JSON then please follow __camelCase__ to maintain the consistency.

6. Searching, sorting, filtering and pagination. We need to append the __query params__ with the GET method API.

refer [RESTful API Designing guidelines — The best practices](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9) for more.