import numpy as np
import pandas as pd
import pickle
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

X = np.loadtxt("X.csv")
y = np.loadtxt("y.csv")

# Read YAML file
with open("params.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

print(data_loaded)
test_size = data_loaded['train']['test_size']
random_state = data_loaded['train']['random_state']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.25, random_state=23
# )
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state
)

lr = LogisticRegression(C=1.0)
lr.fit(X_train.reshape(-1, 1), y_train)

preds = lr.predict(X_test.reshape(-1, 1))
f1 = f1_score(y_test, preds)
print(f"F1 score: {f1:.4f}")

# save the model to disk
filename = 'model.pkl'
pickle.dump(lr, open(filename, 'wb'))