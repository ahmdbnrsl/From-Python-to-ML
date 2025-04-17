from flask import Flask, request
import pickle
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

app = Flask(__name__)


with open('models/model_numpy.pkl', 'rb') as f:
    loaded_pipe_numpy = pickle.load(f)

with open('models/model_pandas.pkl', 'rb') as f:
    loaded_pipe_pandas = pickle.load(f)


@app.route('/')
def index():
    return {"status": "ok", "message": "Success"}, 200


@app.route('/predict/numpy')
def predict_numpy():
    args = request.args
    sl = args.get('sl', default=3.0, type=float)
    sw = args.get('sw', default=3.0, type=float)
    pl = args.get('pl', default=3.0, type=float)
    pw = args.get('pw', default=3.0, type=float)
    new_data = [[sl, sw, pl, pw]]
    predictions = loaded_pipe_numpy.predict(new_data)
    nama = iris.target_names[predictions[0]]
    return {"status": "ok", "input": new_data, "result": "Iris " + nama}, 200


@app.route('/predict/pandas')
def predict_pandas():
    args = request.args
    sl = args.get('sl', default=3.0, type=float)
    sw = args.get('sw', default=3.0, type=float)
    pl = args.get('pl', default=3.0, type=float)
    pw = args.get('pw', default=3.0, type=float)
    new_data = pd.DataFrame([[sl, sw, pl, pw]], columns=iris.feature_names)
    predictions = loaded_pipe_pandas.predict(new_data)
    nama = iris.target_names[predictions[0]]
    return {"status": "ok", "input": {
            "sepal length (cm)": sl,
            "sepal width (cm)": sw,
            "petal length (cm)": pl,
            "petal width (cm)": pw
            }, "result": "Iris " + nama}, 200


app.run(host='0.0.0.0', port=80, debug=True)
