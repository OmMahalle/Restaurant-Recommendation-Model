import joblib
import numpy as np
import pandas as pd
# Load the saved model from a file

def price(predictions1):

    loaded_model = joblib.load('C:\\Users\harsh\PycharmProjects\swiggy_model\mainIMP\Model\dishprice.joblib')
    testdata1 = "C:\\Users\harsh\PycharmProjects\swiggy_model\mainIMP\Model\\test.csv"
    tf = pd.read_csv(testdata1)
    testdata = np.array(tf)
    testdata = testdata.reshape(len(testdata), -1)
    print(testdata)
    predictions1 = loaded_model.predict(testdata)
    # print(predictions1)
    return predictions1
predictions1 = ""
price1 = price(predictions1)
print(price1)
