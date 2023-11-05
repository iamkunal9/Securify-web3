from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
import pickle
import json


with open("db/scam.json", 'r') as json_file:
    scam_bytecodes = json.load(json_file)
with open("db/non_scam.json", 'r') as json_file:
    non_scam_bytecodes = json.load(json_file)

all_bytecodes = scam_bytecodes + non_scam_bytecodes

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(all_bytecodes)

y = [1]*len(scam_bytecodes) + [0]*len(non_scam_bytecodes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier()


parameters = {'n_estimators': [10, 50, 100, 200], 'max_depth': [5, 10, 20, 30, 50]}

cv = ShuffleSplit(n_splits=3, test_size=0.3, random_state=0)

clf = GridSearchCV(model, parameters, cv=cv)
clf.fit(X_train, y_train)

with open('trained/model.pkl', 'wb') as f:
    pickle.dump(clf.best_estimator_, f)
with open('trained/vectorizer.pickle','wb') as f:
    pickle.dump(vectorizer, f)
