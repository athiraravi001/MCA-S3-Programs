"""
1) One-Hot Encoding (Binary Encoding):
   - Converts each category into a binary vector (0s and 1s).
   - Used for Nominal (unordered) categorical variables.
   - Increases number of columns.

2) Label Encoding (Ordinal Encoding):
   - Assigns each category an integer value.
   - Used for Ordinal (ordered) categorical variables.
   - If used on unordered data, it falsely implies ranking.
"""

import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# ------------------- ONE-HOT ENCODING -------------------
data = np.array([['small'], ['medium'], ['large']])   # 2D for One-Hot Encoding

print("Original Data for One-Hot Encoding:\n", data)

onehot_encoder = OneHotEncoder(sparse_output=False)
onehot_encoded = onehot_encoder.fit_transform(data)

print("\nOne-Hot Encoded Result:\n", onehot_encoded)

# onehot_decoded = onehot_encoder.inverse_transform(onehot_encoded)
# print("\nDecoded from One-Hot Encoding:\n", onehot_decoded)

# ------------------- LABEL ENCODING -------------------
labels = np.array(['small', 'medium', 'large'])   # 1D for Label Encoding

print("\nOriginal Data for Label Encoding:\n", labels)

label_encoder = LabelEncoder()
label_encoded = label_encoder.fit_transform(labels)

print("\nLabel Encoded Result:\n", label_encoded)

# decoded_labels = label_encoder.inverse_transform(label_encoded)
# print("\nDecoded Labels:\n", decoded_labels)


# ---------------------------------------------------------

"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({'Size': ['small', 'medium', 'large']})
print("\nPandas DataFrame:", df)

# ------------------- ONE-HOT ENCODING -------------------
df_onehot = pd.get_dummies(df, columns=['Size'])
print("\nOne-Hot Encoding:", df_onehot)

df_onehot['Decoded_Size'] = df_onehot.idxmax(axis=1).str.replace('Size_', '')
print("\nDecoded Back from One-Hot Encoding:", df_onehot)

# ------------------- LABEL ENCODING -------------------
label_encoder = LabelEncoder()
df['Size_Label_Encoded'] = label_encoder.fit_transform(df['Size'])

print("\nLabel Encoding:", df)

df['Decoded_Size'] = label_encoder.inverse_transform(df['Size_Label_Encoded'])
print("\nDecoded Back from Label Encoding:")
print(df)
"""