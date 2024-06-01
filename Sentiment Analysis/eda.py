# This is for EDA for the IMDB movie review

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split 

# define the dataset path
dataset_path = '/media/mahfuz/Media/datasets/IMDB_movie_review/imdb_movie_review_dataset/IMDB_Dataset.csv'
# read and load data from the csv file
data = pd.read_csv(dataset_path)
# define the data set category
X, y =data['review'].values, data['sentiment'].values

# train and test dataset split
x_train, x_test, y_train, y_test = train_test_split(X, y, stratify=y)
print(f'Train data shape: {x_train.shape}')
print(f'Test data shape: {x_test.shape}')



# show the dataset distribution
dd = pd.Series(y_train).value_counts()
sns.barplot(x=np.array(['negative','positive']),y=dd.values) # using seaborn
plt.show()