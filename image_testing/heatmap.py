# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# create data
df = pd.DataFrame(np.random.randn(10,10))
print(df) 
# make it discrete

df_q = pd.DataFrame()
for col in df:
   df_q[col] = pd.to_numeric( pd.qcut(df[col], 3, labels=list(range(3))) )
 
# plot it
sns.heatmap(df_q)
plt.show()
