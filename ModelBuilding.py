import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

def predict(testing):

        df = pd.read_csv(testing)
        print(df)
        x_train= np.array(df.drop(['targetLocation'], 1))
        # print("X=", x_train)

        y_train = np.array(df['targetLocation'])
        # print("y=", y_train)



        clf1 = RandomForestClassifier()
        clf1.fit(x_train, y_train)  # build train model
        joblib.dump(clf1, '../mainIMP/Model/Location.joblib')



predict("../mainIMP/Model/PredictLocation.csv")