import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris_frame = load_iris(as_frame=True)

X, y = iris.data, iris.target

# create pipeline

pipe_numpy = make_pipeline(StandardScaler(), LinearSVC())
pipe_pandas = make_pipeline(StandardScaler(), LinearSVC())

# training

df = iris_frame.frame


# split_dataset
# numpy
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=46)


# pandas
df_train, df_test = train_test_split(df, test_size=0.2, random_state=46)

# training
# numpy
pipe_numpy.fit(X_train, y_train)
y_pred = pipe_numpy.predict(X_test)

print("Classification Report: \n")
print(classification_report(y_test, y_pred))

# pandas
X_train_df, y_train_df = df_train.drop(['target'], axis=1), df_train['target']
X_test_df, y_test_df = df_test.drop(['target'], axis=1), df_test['target']

pipe_pandas.fit(X_train_df, y_train_df)
y_pred_df = pipe_pandas.predict(X_test_df)

print("Classification Report: \n")
print(classification_report(y_test_df, y_pred_df))

# save model
# with open('model_numpy.pkl', 'wb') as f:
#     pickle.dump(pipe_numpy, f)

# with open('model_pandas.pkl', 'wb') as f:
#     pickle.dump(pipe_pandas, f)

# load model
with open('model_numpy.pkl', 'rb') as f:
    loaded_pipe_numpy = pickle.load(f)

with open('model_pandas.pkl', 'rb') as f:
    loaded_pipe_pandas = pickle.load(f)

new_data = [[5.1, 3.5, 1.4, 0.2]]
predictions_numpy = loaded_pipe_numpy.predict(new_data)

new_data = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=iris.feature_names)

predictions_pd = loaded_pipe_pandas.predict(new_data)

print(iris.target_names[predictions_numpy])
print(iris.target_names[predictions_pd])
