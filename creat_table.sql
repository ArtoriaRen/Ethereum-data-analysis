use ethereum_pool_mining;
-- -----------table for blocks-------------
create table block_miner_time
(block_hash char(64) primary key not null,
 miner_address varchar(40) not null,
 block_time timestamp not null
 );
 
alter table block_miner_time
modify column  miner_address char(40);
 
drop table block_miner_time;

-- delete all records in the table 
delete from block_miner_time;
 
insert into block_miner_time(block_hash, miner_address, block_time)
	values('dfe2e70d6c116a541101cecbb256d7402d62125f6ddc9b607d49edc989825c64', 'bb7b8287f3f0a933474a79eae42cbca977791171', '2017-09-06 04:02:15');
    
select count(*) from block_miner_time;
delete from block_miner_time where block_hash='dfe2e70d6c116a541101cecbb256d7402d62125f6ddc9b607d49edc989825c64';

-- -----------table for pools-------------
create table pools
(address char(40) primary key not null,
 pool_name varchar(40) not null
 );
 
select * from pools;

drop table	pools;
delete from pools where pool_name='F2pool 1';
 
insert into pools(address, pool_name)
	values('829bd824b016326a401d083b33d092293333a830', 'F2pool_2');
    
insert into pools(address, pool_name)
	values('5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c', 'SparkPool');

insert into pools(address, pool_name)
	values('ea674fdde714fd979de3edf0f56aa9716b898ec8', 'Ethermine');
    
insert into pools(address, pool_name)
	values('2a5994b501e6a560e727b6c2de5d856396aadd38', 'PandaPool'); -- also known  as pandaminer
    
insert into pools(address, pool_name)
	values('52bc44d5378309ee2abf1539bf71de1b7d7be3b5', 'NanoPool');
        
insert into pools(address, pool_name)
	values('35f61dfb08ada13eba64bf156b80df3d5b3a738d', 'FirePool');
    
insert into pools(address, pool_name)
	values('09ab1303d3ccaf5f018cd511146b07a240c70294', 'MinerAllPool');
    
insert into pools(address, pool_name)
	values('2a65aca4d5fc5b5c859090a6c34d164135398226', 'DwarfPool_1');
    
insert into pools(address, pool_name)
	values('b2930b35844a230f00e51431acae96fe543a0347', 'MiningPoolHub');
    
insert into pools(address, pool_name)
	values('eea5b82b61424df8020f5fedd81767f2d0d25bfb', 'BtccomPool');
    
insert into pools(address, pool_name)
	values('04668ec2f57cc15c381b461b9fedab5d451c8f7f', 'Zhizhu.top');
    
insert into pools(address, pool_name)
	values('06b8c5883ec71bc3f4b332081519f23834c8706e', 'MiningExpress');
    
insert into pools(address, pool_name)
	values('f3b9d2c81f2b24b0fa0acaaa865b7d9ced5fc2fb', 'BitClubPool');
    
insert into pools(address, pool_name)
	values('9435d50503aee35c8757ae4933f7a0ab56597805', 'WaterholePool');

insert into pools(address, pool_name)
	values('52e44f279f4203dcf680395379e5f9990a69f13c', 'BW');

insert into pools(address, pool_name)
	values('6a7a43be33ba930fe58f34e07d0ad6ba7adb9b1f', 'Coinotron_3');

insert into pools(address, pool_name)
	values('4bb96091ee9d802ed039c4d1a5f6216f90f81b01', 'EthPool_2');
insert into pools(address, pool_name)
	values('00192fb10df37c9fb26829eb2cc623cd1bf599e8', '2miners');
insert into pools(address, pool_name)
	values('fa927f196a46067ca3aee3edcaaabce7ef77bb26', 'AntPool');
insert into pools(address, pool_name)
	values('151255dd9e38e44db38ea06ec66d0d113d6cbe37', 'DwarfPool_2');
insert into pools(address, pool_name)
	values('8fce1ef27f3add1411c7a99be402de598ad38389', 'EthashPool_1');
insert into pools(address, pool_name)
	values('29577504e1240b05edb60224759af049c088f68c', 'EthashPool_2');
insert into pools(address, pool_name)
	values('d0db3c9cf4029bac5a9ed216cd174cba5dbf047c', 'Hashon');
insert into pools(address, pool_name)
	values('6c3183792fbb4a4dd276451af6baf5c66d5f5e48', 'MaxHash');
insert into pools(address, pool_name)
	values('44fd3ab8381cc3d14afa7c4af7fd13cdc65026e1', 'Whalesburg_1');
insert into pools(address, pool_name)
	values('7c6694032b4db11ac485e1cff0f7509d58b41569', 'Whalesburg_2');
insert into pools(address, pool_name)
	values('1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe', 'Suprnova');
insert into pools(address, pool_name)
	values('63a9975ba31b0b9626b34300f7f627147df1f526', 'Eth.suprnova.cc');
insert into pools(address, pool_name)
	values('433022c4066558e7a32d850f02d2da5ca782174d', 'AltPool');
insert into pools(address, pool_name)
	values('61c808d82a3ac53231750dadc13c777b59310bd9', 'F2pool_1');

insert into pools(address, pool_name)
	values('61bb630d3b2e8eda0fc1d50f9f958ec02e3969f6', 'MiningPoolHub_5');
insert into pools(address, pool_name)
	values('1a060b0604883a99809eb3f798df71bef6c358f1', 'MiningPoolHub_2');
insert into pools(address, pool_name)
	values('215c86bc952b0d98c4b2313a0a9ae56fa33c7f5d', 'Ethermine.ru');


