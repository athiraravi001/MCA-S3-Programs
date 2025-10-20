# The table below gives the ratings given by 5 users for three food items. Perform SVD on this rating matrix and keep the top k singular values to create a low-rank approximation

          # Pizza   # Burger # Noodles
# User1     5         3        0
# User2     4         0        0
# User3     1         1        0
# User4     0         1        5
# User5     0         0        4

import numpy as np
rating_matrix = np.array([[5, 3, 0], [4, 0, 0], [1, 1, 0], [0, 1, 5], [0, 0, 4]])
u, s, v = np.linalg.svd(rating_matrix)
print("\n===== U =====\n", u)     # first k user latent vectors (relation between 5 users)
print("\n===== S =====\n", s)     # diagonal matrix of top k singular values (relation between users and items)
print("\n===== V =====\n", v)     # first k item latent vectors (relation between items)
k = 2
u_k = u[:,:k]
s_k = np.diag(s[:k])
v_k = v[:k,:]
print("\n===== Low-rank approximation with k singular values =====")
low_rank_approx = np.dot(np.dot(u_k, s_k), v_k)
print(low_rank_approx)