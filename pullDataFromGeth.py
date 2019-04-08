import requests
from requests.exceptions import ConnectionError
import json
import mysql.connector
from datetime import datetime
import threading


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

    def insert_block(self, height, hash_str, miner, timestamp):
        query = 'insert into blockHeight_miner_time(block_height, block_hash, miner_address, block_time) ' \
                'values(\'{}\', \'{}\', \'{}\', \'{}\')'\
            .format(height, hash_str[2:], miner[2:], datetime.fromtimestamp(int(timestamp, 16)))
        # print query
        self.executeQuery(query)


class pull_blocks_thread(threading.Thread):
    def __init__(self, threadID, last_block_hash, last_height, num, client, database):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.last_block_hash = last_block_hash
        self.last_height = last_height
        self.num = num
        self.client = client
        self.database = database

    def run(self):
        self.get_and_store_blocks()

    def get_and_store_blocks(self):
        '''
        Get multiple blocks through rpc to a remote geth client and store the miner and timestamp info into a database.
        :param last_block_hash: hash of the last block to get.
        :param num: the number of blocks to get.
        :param client: rpc client.
        :param database: database to store miner and timestamp info.
        :return: None
        '''
        block = self.last_block_hash
        height = self.last_height
        for i in range(self.num):
            miner, timestamp, parent = self.client.get_miner_timestamp(block)
            # print('Thread'+str(self.threadID), height)
            self.database.insert_block(height, block, miner, timestamp)
            block = parent
            height -= 1



def main():
    num_threads = 32;
    last_block_hashes = ['0x204167e38efa1a4d75c996491637027bb1c8b1fe0d29e8d233160b5256cb415a', # 6100000
                         '0xbe847be2bceb74e660daf96b3f0669d58f59dc9101715689a00ef864a5408f43', # 6000000
                         '0x14962186070395723c2201d1ab0e9685cf84554fdd9e7e50a04c4feb2c627a03', # 5900000
                         '0x5046698811f51b3e55a94c444e6e625f0069b79053f9fafc6b0e57c675863b05', # 5800000
                         '0x3d1d8de9f7ff97b51c3fd9ec706abeae6468b4f907d53838c96c3902ddfafd3c', # 5700000
                         '0x3d3c8fdda26f14ca16e6333066e9f43b54d56d1b0910d8ae35c423e24b9a1e20', # 5600000
                         '0x2d3a154eee9f90666c6e824f11e15f2d60b05323a81254f60075c34a61ef124d', # 5500000
                         '0xca06f5d50466b786d1c85a7062bc4bdda7983f2ff8da3a6dc75e963481d00ffa', # 5400000
                         '0x7923d134566f0e6327964df01567f7b59cc1bc6c0e2b5da30702bc7449bd6178', # 5300000
                         '0x7e7a65e0cedd8d49e6dc6847a93ee66efe0a4146c78f75d6e0e782d5cbd4ac51', # 5200000
                         '0x2059aa02ec74fd52c10323bf26fbdfa284912a66d78147c21e951ecdc5cae750', # 5100000
                         '0x7d5a4369273c723454ac137f48a4f142b097aa2779464e6505f1b1c5e37b5382', # 5000000
                         '0x2f5b03da50161569611ac815ab9f38e67a1353f47b6e5820f5e59334a631298b', # 4900000
                         '0x047d5b3aba8e85b61c1ae9eb8ab96bb2b0e1dc6bfc780fd58d5132dd0adbb728', # 4800000
                         '0x21d53c61a4af67a774e2b6f65ed1bebc1cf043364cf9a36261d24b47516f529a', # 4700000
                         '0x732e35a724de82cba6ccb81d2bd71bc461b16430fe9b0ecfeabf4d1fc77d731e', # 4600000
                         '0x43340a6d232532c328211d8a8c0fa84af658dbff1f4906ab7a7d4e41f82fe3a3', # 4500000
                         '0x432e0067ea0485d28e003c4183a54258dd21460778d494490c905e711fe808ad', # 4400000
                         '0x00003308afe974492f10f946e3f427ef472df07d68739d115bc640288458be59', # 4300000
                         '0xefb6a61b9f7336d559b632940bc9bdfeff589c2be3a7dad6a42b7bf1afa5a33d', # 4200000
                         '0xa108580144142887e58cf074d4ea0be93b00c13ed1992d3897edb078fabe7118', # 4100000
                         '0xb8a3f7f5cfc1748f91a684f20fe89031202cbadcd15078c49b85ec2a57f43853', # 4000000
                         '0xc5e334336b0b40f4ac76aa36c92d0a35d8612a0201de62ad0365ba58bfbb31a1', # 3900000
                         '0x21f423ddc160f0e0f8ca5fa89cb6f7e0e16209a34967d731f52bcbc22d6cab7f', # 3800000
                         '0x0f5dd223d45f24ec5b10d272c987a9463a48b65589150ab62fccad9c0774765d', # 3700000
                         '0xbc9b82594c32aaee97caadfcc4d460aad0824adbc75020565254caaf73659d98', # 3600000
                         '0xc6470e45371f32fb889442dc8f90cea618be575670f65e97f2097bd88ae0a765', # 3500000
                         '0x1f501822bde0f39520315fd8519ab24505c16274c9362f4ea42374c3d2ba2b22', # 3400000
                         '0x750b88eb32e95294dcac85fe09e0f80efac87b03439a7a1a0af924a88e695eb7', # 3300000
                         '0xf06dd7ce1b0162cef3c88145c6531f4868fc849bfeb484e05437da647a6cc990', # 3200000
                         '0xce3399f53ce49c048448aab430995eee6d4ab9107a4aa94d378ae47751e7986f', # 3100000
                         '0xee396a86beaade9d6057b72a92b7bf5b40be4997745b437857469557b562a7c3', # 3000000
                         ]
    last_block_height = 6100000
    client = EthJsonRpc('129.97.105.63', '8332')
    database_objects = []
    for i in range(num_threads):
        db = DB()
        db.open_conn('localhost', 'ethereum_pool_mining', 'root', 'UofW2016')
        database_objects.append(db)
    # get blocks from <last_block_height> to <first_block_height> and store them into database.
    # From Jan 2017 to July 2018: block height 2913667~ 6066958
    threads = []
    for i in range(num_threads):
        sub_last_block = last_block_height- i*100000
        t = pull_blocks_thread(i,
                              last_block_hashes[i],
                              sub_last_block,
                              100000,
                              client=client,
                              database=database_objects[i]
                               )
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    for db in database_objects:
        db.close_conn()

if __name__ == '__main__':
    main()

