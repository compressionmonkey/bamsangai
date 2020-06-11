import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (20,10)

df = pd.read_csv("datasets_1869_18570_bitcoin_cash_price.csv")
price = df.Close
date = df.Date
date_format = pd.get_dummies(date)
# df_bitcoin = pd.concat([price, date_format], axis="columns")

# df_bitcoin.to_csv('test.csv')
X_train, X_test, y_train, y_test = train_test_split(date_format,price,test_size=0.2, random_state=10)
# print(X_train,y_train)

prediction = LinearRegression()
prediction.fit(X_train,y_train)
prediction.score(X_test,y_test)
print(prediction.score(X_test,y_test))

crossvalid = ShuffleSplit(n_splits=5,test_size=0.2, random_state=0)

print(cross_val_score(LinearRegression(), date_format, price, cv=crossvalid))

def find_best_model_using_gridsearchcv(x,y):
    algos = {
        'linear_regression': {
            'model': LinearRegression(),
            'params': {
                'normalize': [True, False]
            }
        },
        'lasso': {
            'model': Lasso(),
            'params': {
                'alpha': [1,2],
                'selection': ['random', 'cyclic']
            }
        },
        'decision_tree': {
            'model': DecisionTreeRegressor(),
            'params': {
                'criterion': ['mse', 'friedman_mse'],
                'splitter': ['best', 'random']
            }
        }
    }
    scores = []
    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
    for algo_name, config in algos.items():
        gs = GridSearchCV(config['model'], config['params'], cv=cv, return_train_score=False)
        gs.fit(date_format, price)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params': gs.best_params_
        })

    final = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
    final.to_csv("final.csv")

find_best_model_using_gridsearchcv(date_format,price)

def predict_price(dates,price):
    date_index = np.where(date_format.columns == dates)[0][0]

    x = np.zeros(len(date_index.columns))
    if date_index >= 0:
        x[date_index] = 1

    return prediction.predict([x])[0]

predict_price('Feb 20, 2018', 1000)
# print(cross_val_score(LinearRegression(), date_format, price, cv=crossvalid))