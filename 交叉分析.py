import numpy as np
import pandas as pd
import matplotlib.pyplot
import seaborn
import scipy.stats

df=pd.read_csv("C:/Users/Administrator/Desktop/DATA/HR.csv")
'''
dp_indices=df.groupby(df["department"]).indices
#print(dp_indices)
sales_values=df['left'].iloc[dp_indices['sales']].values
technical_values=df['left'].iloc[dp_indices['technical']].values
#print(scipy.stats.ttest_ind(sales_values,technical_values)[1])
dp_keys=list(dp_indices.keys())
dp_t_mat=np.zeros([len(dp_keys),len(dp_keys)])
for i in range (len(dp_keys)):
    for j in range (len(dp_keys)):
        p_value=scipy.stats.ttest_ind(df['left'].iloc[dp_indices[dp_keys[i]]].values,
                                        df['left'].iloc[dp_indices[dp_keys[j]]].values)[1]
        if p_value<0.5:
            dp_t_mat[-1]
        else:
            dp_t_mat[i][j]=p_value
seaborn.heatmap(dp_t_mat,xticklabels=dp_keys,yticklabels=dp_keys)
matplotlib.pyplot.show()
'''
#透视图
piv_tb=pd.pivot_table(df,values='left',index=["promotion_last_5years","salary"],\
        columns=["Work_accident"],aggfunc=np.mean)
seaborn.heatmap(piv_tb,vmin=0,vmax=1)
matplotlib.pyplot.show()
