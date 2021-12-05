import pandas as pd
import numpy as np
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score

import xgboost as xgb
import pickle

import warnings
warnings.filterwarnings("ignore")

df_train = pd.read_csv('new_train.csv')
df_train['y'] = df_train['y'].map({'yes': 1, 'no': 0})

df_train.drop('pdays', axis = 1, inplace = True)
df_train.drop('previous', axis = 1, inplace = True)

df_train.drop('y', axis = 1, inplace = True)

df_train, df_val, y_train, y_val = train_test_split(df_train, y, test_size = 0.2)

dv = DictVectorizer(sparse=False)
train_dict = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

val_dict = df_val.to_dict(orient='records')
X_val = dv.transform(val_dict)

features = dv.get_feature_names()
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)
dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)

watchlist = [(dtrain, 'train'), (dval, 'val')]

xgb_params = {
    'eta': 0.1, 
    'max_depth': 5,
    'min_child_weight': 3,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,

    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, num_boost_round=100, evals=watchlist, verbose_eval=10)

output_file = 'model.pkl'

f_out = open(output_file, 'wb') 
pickle.dump((dv, model), f_out)
f_out.close()