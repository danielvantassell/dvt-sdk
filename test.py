from src.client.client import TheOneAPIClient
from src.sdk import TheOneSDK
import os


api_key = os.getenv('THE_ONE_API_KEY')
sdk = TheOneSDK(api_key)
sdk.client.logger.set_level('info')

# Get all movies
#movies = sdk.movies.get_all()
# test_1 = sdk.movies.get_all(sort='name')
# test_2 = sdk.movies.get_all(sort='name:desc')
# test_3 = sdk.movies.search(name='The two Towers')
#import ipdb; ipdb.set_trace()


# Search for movies by title
#movies = sdk.movies.search(name='the return Of the King')
