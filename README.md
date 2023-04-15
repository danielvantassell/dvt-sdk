TheOneAPI provides methods to interface with TheOneAPI service. The API has two layers: The client layer and the API layer. The client layer is responsible for the authentication and communication with the TheOneAPI service, while the API layer provides an interface for interacting with the TheOneAPI endpoints.

TheOneAPI client uses the Requests library to communicate with TheOneAPI service. It has two methods: get and post for making HTTP GET and POST requests to the TheOneAPI service.

Importing the library
To use TheOneAPI, start by installing the required dependencies by running:

bash
Copy code
pip install requests
Then, you can import the library in your Python project as follows:

python
Copy code
from theoneapi.client.client import TheOneAPIClient
from theoneapi.api.movies import MoviesAPI
Initializing TheOneAPIClient
To use TheOneAPI, you must first create an instance of TheOneAPIClient by providing your API key.

python
Copy code
api_key = 'my_api_key'
client = TheOneAPIClient(api_key)
The api_key parameter is mandatory and must be a valid API key.

Initializing MoviesAPI
Once you have an instance of TheOneAPIClient, you can use it to create an instance of the MoviesAPI class.

python
Copy code
movies_api = MoviesAPI(client)
The movies_api instance provides methods for interfacing with TheOneAPI's movies endpoint.

Using MoviesAPI
The movies_api instance provides the following methods:

search
This method searches for movies by name. Only movies with an exact character name match will be matched. Search is case-insensitive.

python
Copy code
movies_api.search(name='The Two Tower')
This method takes the following parameters:

name (required): The name of the movie to search for.
limit (optional): The maximum number of results to return.
page (optional): The page of results to return.
offset (optional): The number of results to skip before starting to return results.
sort (optional): The field to sort the results by.
Example usage:

python
Copy code
# Search for all movies with the exact name 'TWO TOWER'
results = movies_api.search(name='TWO TOWER') # This will not find any results.

# Search for all movies with the exact name 'THE TWO TOWERS'
results = movies_api.search(name='The Two Tower') # Results for The Two Towers will be found

# Search for all movies with the exact name 'the return of the king',
# and sort by release date in ascending order
results = movies_api.search(name='the return of the king', limit=10, sort='release_date')
