# fetch data from different API and convert it to pandas dataframe

If we want to fetch data from API of different source, we need to check if the website gives the API support or not. If it support API service the we can easily fetch data from the API source. 

To fetch data from any API we need one things that is ```api_key``` or ```token access key```. 

we need to login any website and generate the API instruction by that website and generate the ```api_key```. 

Then we can go for coding. Let's go...
```python
import pandas as pd
import requests
for i in range(1, len(pages)):
    # get the url response
    responce = requests.get(f'api url with page{i}')
    # make a dataframe of each page
    temp_df = pd.DataFrame(response.json()['list_name'])['use_col']
    # append dataframe with main dataframe
    df = df.append(temp_df, ignore_index=True)

df.shape # check the shape
df.to_csv('file.csv') # save a csv file
```