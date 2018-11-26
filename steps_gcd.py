
#Jason Mohabir

import math
# library                                                                                                                                                   
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def gcd(x ,y):
   step = 0
   while(y):
      step += 1
      x, y = y, x % y
   return step

rows_list = []
for i in range(0,500):
   dict = {}
   for j in range(0,500):
      d1 = {j: gcd(i,j)}
      dict.update(d1)
   rows_list.append(dict)
#print(rows_list)
df = pd.DataFrame(rows_list)
print(df)

sns.heatmap(df)
plt.show()


