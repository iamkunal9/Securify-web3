from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
import pickle
from bytecode import getByteCode
from flask import Flask, render_template, request



with open('trained/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('trained/vectorizer.pickle', 'rb') as f:
    vectorizer = pickle.load(f)


def predict_scam(bytecode):
    bytecode = vectorizer.transform([bytecode])
    prediction = model.predict(bytecode)
    if prediction == 1:
        return "Scam"
    else:
        return "Not a scam"
# 0x90a16ebcf1bc0da0347134f707da93c40bb8a4c5 scam

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bytecode = ""
    resp = ""
    
    if request.method == 'POST':
        address = request.form.get('address')
        if address:
            bytecode = getByteCode(address, "eth")
            resp = predict_scam(bytecode)
            print(resp)

    return render_template('index.html', bytecode=bytecode, resp=resp)

app.run()
