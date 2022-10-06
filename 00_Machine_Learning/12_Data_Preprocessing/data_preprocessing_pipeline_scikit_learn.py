import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV

np.random.seed(42)

# define X and y
df = gender
X = df.drop(['label', 'gender'], axis=1)
y = df.label



numeric_features = ['income', 'college', 'social', 'vaccine']
numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])

categorical_features =['age', 'gender_new', 'race', 'MIS', 'OBESITY', 'ORGAN', 'DB1', 'DB2', 'MENINGITIS', 'NEUROMSCULAR', 'KINDEY', 'CEREBRAL', 'ENCEPHALITIS', 'KAWASAKI', 'ARRHYTHMIA', 'CONGENITAL', 'CARDIOMYOPATHY', 'PERICARDIAL', 'PERICARDITIS', 'MYOCARDITIS']
features = numeric_features + categorical_features
categorical_transformer = Pipeline(steps=[
('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

clf = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())])
cv = clf.fit(X,y)
categorical_names = clf['preprocessor'].transformers_[1][1]['onehot'].get_feature_names(categorical_features)
names = numeric_features + categorical_names.tolist()

prediction = cv[:-1].transform(df)
df1 = pd.DataFrame(prediction, columns=names, index=df.index)
print(categorical_names.tolist())
df1['label'] = df.label
# df3 = pd.DataFrame(data = df2[1:, 1:], index = df2[1:, 0], columns=df.columns)
