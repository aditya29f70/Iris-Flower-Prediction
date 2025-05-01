from sklearn.datasets import load_iris
import joblib
ir_ds= load_iris()
X= ir_ds.data 
y= ir_ds.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LogisticRegression
model= LogisticRegression()

model.fit(X_train, y_train)

joblib.dump(model, 'iris_model.txt')


