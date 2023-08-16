# Data Acquisition

## working with csv
Data often use in csv file and we need to play with this data.
1. **Read data using ```pandas``` library**
```python
import pandas as pd
df = pd.read_csv
```
2. **Read a csv file from an URL**
```python
import requests
from io import StringIO

url = "row file of url_path/name.csv"

req = requests.get(url=url)
data = StringIO(req.text)

df1 = pd.read_csv(data)
df1.head()
```
3. **Seperate parameters**

we need to use a ```sep``` parameter in the ```pd.read_csv``` file. On that section we will see how to read using ```sep=``` parameters.

Also, ```names``` parameter use for name the colums seperately.

```python
pd.read_csv(name.csv, sep=',', names=['col_name','col_name2'])
```
4. **index_col** parameter

this parameter use for make a column as index, if we put the name of any column in ```index_col``` parameters, it will make the column as index

```python
pd.read_csv('name.csv', index_col='col_name')
```
5. **```header``` parameter**

use ```header``` parameter to filter data. 
```python
pd.read_csv('name.csv', header=row_number)
```
6. **```usecols``` parameter**

```usecols``` parameter use for columns we will need to use in ML operation.
```python
pd.read_csv('file_path/file.csv',usecols=['col_name','col_name1','col_name2'])
```
7. **```squeeze```** parameters 

this parameter use to make a series of any column.
```python
pd.read_csv('file.csv',usecols=['col_name'],squeeze=True)
```
8. ```skiprows/nrow``` parameters

this parameter use to skip any row number or column

```python
pd.read_csv('file.csv', skiprows=[0, 1])

pd.read_csv('file,csv', nrows=100)
```
8. **```encoding```** parameter

Make the encoding systems of a datasets.

```python
pd.read_csv('file.csv',encoding='utf-8')
```
9. **```dtype```** parameter

Use for transform a data dype in certain data type. 
```python
pd.read_csv('file.csv', dtype={'col_name':int/str etc})
```
10. **Handling date (```parse_dates```)**

to convert any str/object data type to data format. 
```python
pd.read_csv('catalog.csv', parse_dates=['date'])
```
11. **```converter```** parameter

Use to convert any str/int value to any type of systax. 
```python
def rename(name):
    if name == 'United States':
        return 'US'
    else:
        return name

# print(rename('United States'))
pd.read_csv('catalog.csv', converters={'col_name':rename})
```
12. **```na_values``` parameter**

use any values to NaN tyep value. 
```python
pd.read_csv('file.csv', na_values={'col_name':'value'})
```

13. **Loading a huge dataset in chunks**

when we use large dataset what we will need to load but have not enough RAM in PC. Then we need to use ```chunks``` parameters. 
```python
dfs = pd.read_csv('aug_train.csv', chunksize=1000)

for chunks in dfs:
    print(chunks.shape)
```