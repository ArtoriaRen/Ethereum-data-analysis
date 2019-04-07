import requests
from requests.exceptions import ConnectionError
import json
import mysql.connector
from datetime import datetime


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

    def get_miner_timestamp(self, hash):
        params = [hash, True]
        res = self.call('eth_getBlockByHash', params)
        return res['miner'], res['timestamp'], res['parentHash']


class DB(object):
    '''
    Database connector.
    '''
    def __int__(self):
        self.conn = None

    def open_conn(self, host, database, user, password):
        self.conn = mysql.connector.connect(host=host, database=database, user=user, password=password)

    def close_conn(self):
        self.conn.close()

    def executeQuery(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query, params=None, multi=False)
        self.conn.commit()
        cursor.close()

    def insert_block(self, hash_str, miner, timestamp):
        query = 'insert into block_miner_time(block_hash, miner_address, block_time) values(\'{}\', \'{}\', \'{}\')'\
            .format(hash_str[2:], miner[2:], datetime.fromtimestamp(int(timestamp, 16)))
        # print query
        self.executeQuery(query)


def get_and_store_blocks(last_block_hash, num, client, database):
    '''
    Get multiple blocks through rpc to a remote geth client and store the miner and timestamp info into a database.
    :param last_block_hash: hash of the last block to get.
    :param num: the number of blocks to get.
    :param client: rpc client.
    :param database: database to store miner and timestamp info.
    :return: None
    '''
    block = last_block_hash
    for i in range(num):
        miner, timestamp, parent = client.get_miner_timestamp(block)
        # print(miner)
        database.insert_block(block, miner, timestamp)
        block = parent



def main():
    client = EthJsonRpc('129.97.105.63', '8332')
    db = DB()
    db.open_conn('localhost', 'ethereum_pool_mining', 'root', 'UofW2016')
    # get blocks from <start_block_height> to <end_block_height> to  6065979 and store them into database.
    # There are <end_block_height>-<start_block_height>+1 blocks.
    get_and_store_blocks('0x40285b650271b10275e50487d855d8357a9a3f21626fda1d255ad9b863b1905e', 6066958-2913667+1, client=client, database=db)
    db.close_conn()

if __name__ == '__main__':
    main()

