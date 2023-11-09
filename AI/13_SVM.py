import numpy as np
from sklearn import datasets 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

x,y = datasets.make_classification(n_samples=1000, n_features=3, n_informative=2, n_redundant=0, random_state=48)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25, random_state=100)

svm_classifier = SVC(kernel='linear', C=1.0)

svm_classifier.fit(x_train, y_train)
y_pred = svm_classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)