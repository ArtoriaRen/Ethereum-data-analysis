-- --------------create a view to match each block with the pool name if they are mined by pool ---------------
create view v_pool_mined_block as select * from blockHeight_miner_time join pools where miner_address=address;
drop view v_pool_mined_block;
select count(*) from v_pool_mined_block;
--             ---------------analyze-------------
--  --------------------how many blocks are mined by pool per month-----------------
select * from (
select year(block_time) as yp, month(block_time) as mp, count(*) from v_pool_mined_block group by year(block_time), month(block_time)
) as pool join (
select year(block_time) as y, month(block_time) as m, count(*) from blockHeight_miner_time group by year(block_time), month(block_time)
) as total on yp=y and mp=m;

-- -----------------------in JAN 2018, what portional of blocks is mined by each pool.--------
select pool_name,count(*) from v_pool_mined_block where year(block_time)='2018' and month(block_time)='07' group by pool_name;


-- -----------------------Fewer blocks are mined around Aug 2017.--------
select * from blockHeight_miner_time where year(block_time)='2017' and month(block_time)='08';