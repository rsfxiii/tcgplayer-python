from configparser import ConfigParser

import requests


class TCGPlayer:
    """
     tcgplayer.src.api.client.TCGPlayer
    
    Handles configuration loading, access grants, and API calls.

    --- AUTH FLOW ---
    1. Read the config into the instance with .read_config()
    2. Retrieve access token with .refresh_access()
    3. Load access data into requests.Session with .authorize_session()

    --- REQUEST FLOW ---
    1. Have valid Session (via Auth Flow above)
    2. Pass endpoint URL to Session w/ options

    """

    base_url = "https://api.tcgplayer.com"

    def __init__(self):
        """ Establish default class properties """
        self._config = {
            'data': None,
            'parser': None
        }
        self._session = {
            'obj': None,
            'access': None
        }

    def read_config(self, config='config.ini', section='Default'):
        """ Load config data into bound dictionary """
        self._config['parser'] = ConfigParser()
        self._config['parser'].read_file(open(config))
    
        if section in self._config['parser'].sections():
            self._config['data'] = dict(self._config['parser'].items(section))

    def refresh_access(self):
        """ Update access attribute with fresh access object """
        url = f'{TCGPlayer.base_url}/token'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": str(self._config['data']['pubkey']),
            "client_secret": str(self._config['data']['privkey'])
        }

        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            self._session['access'] = response.json()

    def authorize_session(self):
        """ Update bound session object with bound access data """
        token = self._session['access']['access_token']

        self._session['obj'] = requests.Session()
        self._session['obj'].headers.update({"Authorization": f"Bearer {token}"})
