import numpy
from sklearn.decomposition import PCA
import pandas
data=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/luqu.csv')
pca1=PCA(2)
pca1.fit(data[1:4])
tz1=pca1.components_
rate=pca1.explained_variance_ratio_
reduction=pca1.transform(data)
