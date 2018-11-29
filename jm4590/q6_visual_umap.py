import sympy
import matplotlib.pyplot as plt
import matplotlib as mp

import numpy as np
import pandas as pd

import datashader as ds
import datashader.utils as utils
import datashader.transfer_functions as tf

import umap
import warnings
warnings.filterwarnings('ignore')

n = 10000

factors = [sympy.factorint(x) for x in range(int(n))]
primes = set()
for fac in factors:
    primes.update(fac.keys())
len(primes)


# sort primes to use as index
primes = sorted(primes)

from scipy import sparse
from tqdm import tqdm_notebook
tqdm = tqdm_notebook

mat = sparse.lil_matrix((int(n), len(primes)), dtype=int)
    
# populate the sparse matrix
for i, fac in enumerate(factors):
        for key, value in fac.items():
            # find index of prime in colum
            col = primes.index(key)
            # insert value (exponent) in position.
            # should I put 1?
        mat[i, col] = value
    
mat_csr = mat.tocsr()
    
# save to disk
#sparse.save_npz('1e6_factors_mat.npz', mat_csr)


reducer = umap.UMAP(metric='cosine', verbose=2, n_epochs=100)

# takes about 2 hours with an i7 7700 ;_;7
embedding = reducer.fit_transform(mat_csr)

np.save('embedding_primes', embedding)

mat = np.load('embedding_primes.npy')

df = pd.DataFrame(mat, columns=['x', 'y'])

cvs = ds.Canvas(plot_width=500, plot_height=500)
agg = cvs.points(df, 'x', 'y')
img = tf.shade(agg, how='eq_hist', cmap=mp.cm.viridis)
tf.set_background(img, 'black')
fig = plt.figure(figsize=(10,10))
fig.patch.set_facecolor('black')
plt.scatter(df.x, df.y, marker='o', s=1, edgecolor='',
            c=df.index, cmap="magma", alpha=0.5)

plt.axis("off")
plt.show()
