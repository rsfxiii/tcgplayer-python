

from configparser import ConfigParser


import requests




class TCGPlayer:
    """
     tcgplayer.src.api.client.TCGPlayer
    
    This object acts as middleware between requests.Session
    and ConfigParser. Use
    
    """


    base_url = "https://api.tcgplayer.com"

    def __init__(self):
        self._config = {
            'data': None,
            'parser': None
        }
        self._session = {
            'obj': None,
            'access': None
        }

    def read_config(self, config='config.ini', section='Default'):
        self._config['parser'] = ConfigParser()
        self._config['parser'].read_file(open(config))
    
        if section in self._config['parser'].sections():
            self._config['data'] = dict(self._config['parser'].items(section))

    def refresh_access(self):
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
        token = self._session['access']['access_token']

        self._session['obj'] = requests.Session()
        self._session['obj'].headers.update({"Authorization": f"Bearer {token}"})
