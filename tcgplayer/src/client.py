import os

import dotenv
import requests


class Client:
    @staticmethod
    def build_access_payload(client_id, client_secret):
        return {
            'grant_type': 'client_credentials',
            'client_id': str(client_id),
            'client_secret': str(client_secret)
        }

    @staticmethod
    def refresh_access_token():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        payload = Client.build_access_payload(os.getenv('PUB_KEY'), os.getenv('PRIV_KEY'))

        response = requests.post('https://api.tcgplayer.com/token', payload, headers)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def handle_request(method, url, data, token=None):

        session = requests.Session()
        if not token:
            print('No access_token provided; executing Client.refresh_access_token')
            token = Client.refresh_access_token()['access_token']

        session.headers['Authorization'] = f"Bearer {token}"
        try:
            response = session.request(method.upper(), url, data)
            return response.json()
        except requests.RequestException:
            raise


# if __name__ == '__main__':
#     dotenv.load_dotenv(dotenv.find_dotenv())
#
#     access_payload = Client.build_access_payload(os.getenv('PUB_KEY'), os.getenv('PRIV_KEY'))
#     print(access_payload)
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
