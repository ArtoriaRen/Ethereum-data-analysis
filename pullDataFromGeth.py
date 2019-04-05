import requests
from requests.exceptions import ConnectionError
import json

class BadResponseError(Exception):
    pass

class EthJsonRpc(object):
    '''
    Ethereum JSON-RPC client class
    '''
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.session = requests.session()

    def call(self, method, params=None, id=1):
        data = {
            "jsonrpc":"2.0",
            "method":method,
            "params":params or [],
            "id": id
        }
        scheme = 'http'
        url = '{}://{}:{}'.format(scheme, self.host, self.port)
        headers = {"Content-Type": "application/json"}
        try:
            r = self.session.post(url=url, headers=headers, data=json.dumps(data)).json()
        except  ConnectionError:
            raise ConnectionError
        try:
            return r['result']
        except KeyError:
            raise BadResponseError(r)

    def get_miner(self, hash):
        params = [hash, True]
        res = self.call('eth_getBlockByHash', params)
        return res['miner']

def main():
    client = EthJsonRpc('129.97.105.63', '8332')
    last_block = '0xdfe2e70d6c116a541101cecbb256d7402d62125f6ddc9b607d49edc989825c64'
    miner = client.get_miner(last_block)
    print(miner)

if __name__ == '__main__':
    main()

