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

        data = {
            'grant_type': 'client_credentials',
            'client_id': str(os.getenv('PUB_KEY')),
            'client_secret': str(os.getenv('PRIV_KEY'))
        }

        response = requests.post('https://api.tcgplayer.com/token', data, headers)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def handle_request(method, url, data, token=None):

        session = requests.Session()
        if not token:
            print('No access_token provided; executing NewClient.refresh_access_token')
            secret = Client.refresh_access_token() # Looking for default .env

        session.headers['Authorization'] = f"Bearer {secret['access_token']}"
        try:
            response = session.request(method.upper(), url, data)
            return response.json()
        except requests.RequestException:
            raise


# if __name__ == '__main__':
#
#     access_token = Client.refresh_access_token()
#     assert access_token is not None
#     print(access_token)
#
#     data = Client.handle_request('GET', 'https://api.tcgplayer.com/catalog/categories', {}, None)
#     print(data)
