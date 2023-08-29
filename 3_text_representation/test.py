#%%
import pandas as pd

df = pd.read_csv('/media/mahfuz/Media/datasets/NLP_learn/data_preprocessing/IMDB_dataset_50k_movie_review/IMDB_Dataset.csv', chunksize=10000)
df.get_chunk(3)
# for data in df:
#     print(data.shape)
#%%
#print(data.shape)

# %%

for data in df:
    print(data.shape)
    data['review'] = data['review'].str.lower()

df.to_csv(tt.csv)
df1 = pd.read_csv(tt.csv)
df1.head()
# %%
