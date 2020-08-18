import os

import dotenv
import requests


class Client:
    @staticmethod
    def refresh_access_token(env_file='.env'):
        dotenv.load_dotenv(env_file or dotenv.find_dotenv())

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        payload = {
            'grant_type': 'client_credentials',
            'client_id': str(os.getenv('PUB_KEY')),
            'client_secret': str(os.getenv('PRIV_KEY'))
        }

        response = requests.post('https://api.tcgplayer.com/token', payload, headers)
        if response.ok:
            return response.json()['access_token']
        else:
            response.raise_for_status()

    @staticmethod
    def handle_request(method, url, data, token=None):

        session = requests.Session()
        if not token:
            print('No access_token provided; executing Client.refresh_access_token')
            token = Client.refresh_access_token() # Looking for default .env

        session.headers['Authorization'] = f"Bearer {token}"
        try:
            response = session.request(method.upper(), url, data)
            return response.json()
        except requests.RequestException:
            raise


# if __name__ == '__main__':
#
#     # I'm getting two errors from Pycharm on this line, but it works?
#     from api.endpoints import Category
#
#     # Refresh your access token for the session
#     access_token = Client.refresh_access_token()
#
#     # Make sure it's there before continuing
#     assert access_token is not None
#
#     # Hell, look at it!
#     print(access_token)
#
#     # Make the call
#     data = Client.handle_request('GET', Category.list(), {}, access_token)
#
#     # See the response data
#     print(data)
