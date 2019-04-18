# Ethereum-data-analysis
This repository should not be set as public at present because the result is presented in a paper which is currently under review.

## `pullDataFromGeth.py`
- Pulls mining-related data from a geth node to local machine via JSON RPC API
- Stores the data in a MySQL database for analysis

## `creat_table.sql` and `create_view.sql`
- Creates tables and views in a MySQL database

## `data` folder
- SQL execution results in CSV format

## `graph` folder
- draw a stacked histogram to illustrat how the number of pool-mined blocks changed using data in `data/ether_monthly_data.csv`

## `pie_chart.py` folder
- draw a pied chart for data in `data/ether_2018_july.csv`
