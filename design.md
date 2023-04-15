# TheOneSDK API Layer Design
##Overview
TheOneSDK is a Python package that provides an API wrapper for TheOneAPI. The API layer is responsible for interfacing with TheOneAPI's endpoints for movies and characters.

# Design Approach
The design approach for the API layer was to create a set of classes that represent each of the endpoints in TheOneAPI. Each class contains methods that correspond to the different API operations that can be performed on that endpoint.

The MoviesAPI class contains methods for interfacing with TheOneAPI's movies endpoint. Similarly, the CharactersAPI class contains methods for interfacing with TheOneAPI's characters endpoint.

# Class Structure
Each API class follows a similar structure:

## Constructor: Takes a TheOneAPIClient object as an argument. The client object is responsible for making the HTTP requests to TheOneAPI's endpoints.
## Methods: The API methods correspond to the different API operations that can be performed on the endpoint. Each method takes a set of arguments that correspond to the parameters for the API operation. The methods return the response from TheOneAPI's endpoint.
## Error Handling
The API layer also includes error handling for when API operations fail. The InvalidSearchKeyError is raised when the search key provided to the MoviesAPI.search() method is not an approved search key.

# Pagination
The API layer also includes pagination functionality for endpoints that return a large number of results. The limit, page, and offset parameters can be used to limit the number of results returned and navigate through the results.

# Future Improvements
In the future, the API layer could be extended to include methods for additional endpoints in TheOneAPI. Additionally, the API layer could be extended to include more error handling and better support for pagination.
