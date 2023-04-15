# dvt-the-one-sdk Design

## Overview
TheOneSDK is a Python package that provides an API wrapper for TheOneAPI. The API layer is responsible for interfacing with TheOneAPI's endpoints for movies and characters.

# Design Approach
The design approach for the API layer was to create a set of classes that represent each of the endpoints in TheOneAPI. Each class contains methods that correspond to the different API operations that can be performed on that endpoint.

The MoviesAPI class contains methods for interfacing with TheOneAPI's movies endpoint. Similarly, the CharactersAPI class contains methods for interfacing with TheOneAPI's characters endpoint.

# Layout:
```
├── src
│   ├── api
│   │   ├── characters.py
│   │   └── movies.py
│   ├── client
│   │   └── client.py
│   ├── common
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── logger.py
│   │   ├── singleton.py
│   │   ├── utils.py
│   │   └── version.py
│   └── sdk.py
└── tests
    ├── mock.py
    ├── test_client.py
    └── test_movies.py
```

# API Layer
The API layer provides a simple interface for interacting with TheOneAPI's movies endpoint. The API provides methods for searching and retrieving movies. The API layer is built on top of TheOneAPIClient, which is responsible for handling the communication with the TheOneAPI server.

# Methods
`search()`
The search() method searches for movies by name. The method only returns movies with an exact match for the provided name. The search is case-insensitive. The method supports pagination, sorting, and additional search parameters.

`get_all()`
The get_all() method retrieves all movies. The method supports pagination, sorting, and additional search parameters.

## Advantages of the API Layer
The API layer provides a simple and easy-to-use interface for interacting with TheOneAPI's movies endpoint. The methods are designed to be intuitive and easy to use, making it easy for developers to get started with the SDK. The API layer also supports pagination, sorting, and additional search parameters, providing flexibility for developers who need to retrieve large amounts of data.

## Trades-off made in the API Layer
The API layer only supports searching and retrieving movies. While this may be limiting for some use cases, it makes the API layer simple and easy to use. Additionally, the API layer only supports searching for movies by name, which may not be suitable for all use cases. However, the API layer can be extended to support additional search parameters if needed.

# TheOneAPIClient
TheOneAPIClient is responsible for handling the communication with the TheOneAPI server. The client is built on top of the requests library and provides methods for making HTTP requests to the TheOneAPI server.

## Advantages of TheOneAPIClient
TheOneAPIClient provides a simple and easy-to-use interface for communicating with the TheOneAPI server. The client is built on top of the requests library, which is a widely-used library for making HTTP requests in Python. The client also provides error handling, making it easy to identify and handle errors that occur during communication with the server.

## Trades-off made in TheOneAPIClient
`TheOneAPIClient` only supports communication with the TheOneAPI server. The client does not provide support for other APIs or services. Additionally, `TheOneAPIClient` only supports version 2 of the TheOneAPI. If the TheOneAPI is updated to a new version, `TheOneAPIClient` will need to be updated to support the new version, and is easily supported.


# Class Structure
Each API class follows a similar structure: `src/<endpoint>/<functionality>`

## Constructor: Takes a TheOneAPIClient object as an argument. The client object is responsible for making the HTTP requests to TheOneAPI's endpoints.
## Methods: The API methods correspond to the different API operations that can be performed on the endpoint. Each method takes a set of arguments that correspond to the parameters for the API operation. The methods return the response from TheOneAPI's endpoint.
## Error Handling
The API layer also includes error handling for when API operations fail. The InvalidSearchKeyError is raised when the search key provided to the MoviesAPI.search() method is not an approved search key.

# Pagination
The API layer also includes pagination functionality for endpoints that return a large number of results. The limit, page, and offset parameters can be used to limit the number of results returned and navigate through the results.



# Future Improvements
Currently, the sdk grows based on endpoint organization, ie: `sdk.movies.search`.  All movie expansions such a s quote or detail view would be expanded by extending additional functionaltiy. This allows logical flow for expanding to more features such as `sdk.movies.quotes` or `sdk.characters.quotes`
