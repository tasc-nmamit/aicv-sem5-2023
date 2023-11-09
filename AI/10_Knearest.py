import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#Generate some random Sample data for calssification
np.random.seed(0)

X = np.random.rand(1000000,2) #Feature Matrix
y = np.random.choice([0, 1], size=1000000) #Target Vector (Binary Classification)

# Split data into train and test
x_train, x_test, y_train, y_test = tts(X,y, test_size=0.2, random_state=42)

#Create K Nearest Neighbors classifier with k=3
k = 3
knn_classifier = KNeighborsClassifier(n_neighbors=k)

#Proceed with training of the model
knn_classifier.fit(x_train,y_train)

#Utilize the model to predict data
y_pred = knn_classifier.predict(x_test)

acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc*100:.2f}%")