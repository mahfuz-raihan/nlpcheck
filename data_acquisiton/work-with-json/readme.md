# work with json/sql file

## 1. work with json file
```pandas``` library can easily ready the json file.
```python
import pandas as pd
print(f'pandas library import successfully')
pd.read_json('file.json')
```
After that, we can follow the ```padas.read_json``` doc for more information, but still the save function and parameter to read a file. 

## 2. work with sql

There are two way to work with sql file
1. using ```psycopg2``` connector
2. using ```SQLAlchemy``` library


### **2.1 ```psycopg2``` library** 
Let's see the two following way. You can fowllow the notebook for more details. but, will show the banchmark here. 

```python
import pandas as pd
import psycopg2 as pg2 
from config import config


# connection configuration
conn = pg2.connect(
    host="host_name",
    database="database_name",
    user="user_name",
    password="your_password"
)

sql = 'select * from table_name'
df = pd.read_sql_query(sql, conn) # read sql statement

conn.close() # close the database connection

df.head()
```

### **2.2 ```SQLAlchemy``` library**
Generally, sqlalchemy is consider by the pandas and this important way should be know. Here, we need to install older version of SQLAlchemy, higher version make e pandas update delay. 

```python
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# make the connection with the connector format
conn = "postgresql+psycopg2://your_user:your_password@your_host:your_port/your_database"
engine = create_engine(conn) # connection engine

sql = 'select * from table_name'
df = pd.read_sql_query(sql, con=engine) # read sql_query

df
```