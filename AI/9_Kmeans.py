import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(0)

# Generate random data with 100 data points in 2D
X = np.random.rand(100, 2)

# Define the number of clusters (k)
k = 3

# Create a KMeans model with k clusters
kmeans = KMeans(n_clusters=k)

# Fit the model to the data, which performs clustering
kmeans.fit(X)

# Get the cluster centers
cluster_centers = kmeans.cluster_centers_

# Get the labels assigned to each data point indicating their cluster
labels = kmeans.labels_

# Create a scatter plot of the data points with color-coded clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)

# Mark cluster centers with 'x' markers in red
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', s=200, color='red')

# Set the title of the plot
plt.title(f'K-Means Clustering (k={k})')

# Display the plot
plt.show()
