# To implement K Means clustering using Iris dataset available in the public domain and find the inertia of the algorithm

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the Iris dataset
df = pd.read_csv(".venv/DataSet/Iris.csv")
X = df.iloc[:, 1:5]   # Select only the feature columns (SepalLength to PetalWidth)

# ===== Determine Optimal k using Elbow Method =====
inertia = []        # List to store inertia values for different k
K = range(1, 11)    # Try k from 1 to 10

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)  # Initialize KMeans
    kmeans.fit(X)                                   # Fit KMeans to data
    inertia.append(kmeans.inertia_)                 # Store inertia (sum of squared distances to centroids)

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(K, inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

# Choose optimal k (manually from elbow plot)
k_elbow = 2  # Replace with actual elbow point observed from the graph

# Train KMeans with optimal k from Elbow Method
kmeans_elbow = KMeans(n_clusters=k_elbow, random_state=42)
kmeans_elbow.fit(X)                            # Fit the model
labels_elbow = kmeans_elbow.labels_            # Cluster assignments for each data point
centers_elbow = kmeans_elbow.cluster_centers_  # Coordinates of centroids

print("----- Clustering using Elbow Method -----")
print("Cluster centers (elbow):\n", centers_elbow)
print("Inertia (elbow method):", kmeans_elbow.inertia_)

# Visualize Elbow Clustering (Scatter plot of PetalLength vs PetalWidth with cluster labels)
plt.figure(figsize=(8,6))
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=labels_elbow, cmap="viridis", s=50, alpha=0.8)
plt.scatter(centers_elbow[:, 2], centers_elbow[:, 3], c="red", s=200, marker="X", label="Centroids")
plt.title(f"KMeans Clustering (Elbow k={k_elbow})")
plt.xlabel("PetalLength")
plt.ylabel("PetalWidth")
plt.legend()
plt.show()

# Predict a new sample using Elbow model
new_point = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=X.columns)
pred_elbow = kmeans_elbow.predict(new_point)
print("Predicted cluster (Elbow k):", pred_elbow[0])

# ===== Determine Optimal k using Silhouette Score =====
sil_scores = []
k_range = range(2, 11)  # Silhouette score cannot be computed for k=1

for k in k_range:
    kmeans_tmp = KMeans(n_clusters=k, n_init=8, random_state=10)   # Fit temporary model
    cluster_labels = kmeans_tmp.fit_predict(X)                     # Assign clusters
    score = silhouette_score(X, cluster_labels)                    # Compute silhouette score
    sil_scores.append(score)

# Plot Silhouette Scores
plt.figure(figsize=(8, 5))
plt.plot(k_range, sil_scores, marker='o')
plt.title("Silhouette Score Method for Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.grid(True)
plt.show()

# Optimal k is the one with max silhouette score
k_silhouette = k_range[sil_scores.index(max(sil_scores))]
print(f"Optimal k (silhouette): {k_silhouette}")

# Train KMeans with optimal k from Silhouette Method
kmeans_sil = KMeans(n_clusters=k_silhouette, random_state=42)
kmeans_sil.fit(X)
labels_sil = kmeans_sil.labels_
centers_sil = kmeans_sil.cluster_centers_

print("----- Clustering using Silhouette Method -----")
print("Cluster centers (silhouette):\n", centers_sil)
print("Inertia (silhouette method):", kmeans_sil.inertia_)

# Visualize Silhouette Clustering
plt.figure(figsize=(8,6))
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=labels_sil, cmap="viridis", s=50, alpha=0.8)
plt.scatter(centers_sil[:, 2], centers_sil[:, 3], c="red", s=200, marker="X", label="Centroids")
plt.title(f"KMeans Clustering (Silhouette k={k_silhouette})")
plt.xlabel("PetalLength")
plt.ylabel("PetalWidth")
plt.legend()
plt.show()

# Predict a new sample using Silhouette model
pred_sil = kmeans_sil.predict(new_point)
print("Predicted cluster (Silhouette k):", pred_sil[0])