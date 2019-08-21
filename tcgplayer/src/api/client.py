from configparser import ConfigParser

import requests


class Client:
    def __init__(self):
        ''' Establish default class properties '''
        self._config = {
            'data': None,
            'parser': None
        }
        self._session = {
            'obj': None,
            'access': None
        }

    def read_config(self, config='config.ini', section='Default'):
        ''' Load config data into bound dictionary '''
        self._config['parser'] = ConfigParser()
        file = open(config, 'r')
        self._config['parser'].read_file(file)
        file.close()
    
        if section in self._config['parser'].sections():
            self._config['data'] = dict(self._config['parser'].items(section))

    def refresh_access(self, refresh_url):
        ''' Update access attribute with fresh access object '''
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': str(self._config['data']['pubkey']),
            'client_secret': str(self._config['data']['privkey'])
        }

        response = requests.post(refresh_url, data=data, headers=headers)
        if response.status_code == 200:
            self._session['access'] = response.json()

    def authorize_session(self):
        ''' Update bound session object with bound access data '''
        token = self._session['access']['access_token']

        self._session['obj'] = requests.Session()
        self._session['obj'].headers.update({'Authorization': f'Bearer {token}'})

    def _handle_request(self, method, url, data=None):
        print(url)
        res = self._session['obj'].request(method.upper(), url, data=data)
        if res.status_code == 200:
            return res.json()
        else:
            print(res.text)

class TCGPlayer:
    '''
     tcgplayer.src.api.client.TCGPlayer
    
    Handles configuration loading, access grants, and API calls.

    --- AUTH FLOW ---
    1. Read the config into the instance with .read_config()
    2. Retrieve access token with .refresh_access()
    3. Load access data into requests.Session with .authorize_session()

    --- REQUEST FLOW ---
    1. Have valid Session (via Auth Flow above)
    2. Pass endpoint URL to Session w/ options

    '''

    api_url = 'https://api.tcgplayer.com'
    endpoint_base = ''

    def __init__(self, client: Client):
        if isinstance(client, Client):
            self.client = client
        else:
            self.client = client()

        self.refresh_url = f'{self.api_url}/token'
        self.base_url = f'{self.api_url}{self.endpoint_base}'

class Categories(TCGPlayer):
    endpoint_base = '/catalog/categories'

    def __init__(self, client, default='1'):
        self.current = str(default) # Default is Magic The Gathering
        super().__init__(client)

    def list(self, data=None):
        return self.client._handle_request('GET', self.base_url, data=data)

    def get_details(self, category_id):
        endpoint = f'{self.base_url}/{category_id}'
        return self.client._handle_request('GET', endpoint)

    def get_search_manifest(self, category_id):
        endpoint = f'{self.base_url}/{category_id}/search/manifest'
        return self.client._handle_request('GET', endpoint)

    def search_products(self, term, category_id):
        endpoint = f'{self.base_url}/{category_id}/search'
        return self.client._handle_request('POST', endpoint, data={'name': str(term)})

    def list_groups(self, category_id):
        endpoint = f'{self.base_url}/{category_id}/groups'
        return self.client._handle_request('GET', endpoint)

    def get_printings(self, category_id):
        endpoint = f'{self.base_url}/{category_id}/printings'
        return self.client._handle_request('GET', endpoint)

    def get_rarities(self, category_id):
        endpoint = f'{self.base_url}/{category_id}/rarities'
        return self.client._handle_request('GET', endpoint)

    def list_conditions(self, category_id):
        endpoint = f'{self.base_url}/{category_id}/conditions'
        return self.client._handle_request('GET', endpoint)

    def list_languages(self, category_id):
        endpoint = f'{self.base_url}/{category_id}/languages'
        return self.client._handle_request('GET', endpoint)

    def list_media(self, category_id):
        endpoint = f'{self.base_url}/{category_id}/media'
        return self.client._handle_request('GET', endpoint)


class Groups(TCGPlayer):
    endpoint_base = '/catalog/groups'

    def __init__(self, client):
        super().__init__(client)

    def list(self, category_id):
        endpoint_base = f'{self.base_url}'
        return self.client._handle_request('GET', self.base_url, data=1)



if __name__ == '__main__':

    # Bootstrap the client
    client = Client()
    client.read_config()

    # Init an API instance w/ Client    
    categories = Categories(client=client)

    client.refresh_access(refresh_url=categories.refresh_url)
    client.authorize_session()


    groups = Groups(client)
    print(groups.base_url)
    # print(groups.list(1))
    
    import urllib.parse as urlparse
    from urllib.parse import urlencode


    parts = list(urlparse.urlparse(groups.base_url))
    params = {'categoryId': 1}

    query = dict(urlparse.parse_qs(parts[4]))
    query.update(params)

    assert query == params

    parts[4] = urlencode(query)
    print(parts)

    print(urlparse.urlunparse(parts))
    

    # TODO: Write tests for these
    # print(categories.list())
    # print(categories.get_details('1'))
    # print(categories.get_search_manifest('1'))
    # print(categories.list_groups('1'))
    # print(categories.get_rarities('1'))
    # print(categories.get_printings('1'))
    # print(categories.list_languages('1'))
    # print(categories.list_media('1'))

    
    
    # import pdb; pdb.set_trace()