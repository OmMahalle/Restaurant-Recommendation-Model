import joblib
import numpy as np
import pandas as pd
# Load the saved model from a file
def locn(key):
    loaded_model = joblib.load('C:\\Users\harsh\PycharmProjects\swiggy_model\mainIMP\Model\Location.joblib')
    testdata1 = "C:\\Users\harsh\PycharmProjects\swiggy_model\mainIMP\Model\\test.csv"
    tf = pd.read_csv(testdata1)
    testdata = np.array(tf)
    testdata = testdata.reshape(len(testdata), -1)
    print(testdata)
    predictions1 = loaded_model.predict(testdata)
    # print(predictions1)
    # Print the predicted labels
    # print(predictions1)



    location_dict ={'ashok-nagar': 1, 'banashankari': 2, 'banaswadi': 3, 'basavanagudi': 4, 'basaveshwara-nagar': 5, 'bel-road': 6, 'bima-nagar': 7, 'bommanahalli': 8, 'brigade-road': 9, 'central': 10, 'chikpete': 11, 'course-road': 12, 'cunningham-road': 13, 'domlur': 14, 'ejipura': 15, 'ganganagar': 16, 'halasuru': 17, 'hebbal': 18, 'hennur': 19, 'indiranagar': 20, 'jaya-nagar': 21, 'jp-nagar': 22, 'kalyan-nagar': 23, 'kammanahalli': 24, 'koramangala': 25, 'lavelle-road': 26, 'HSR-layout': 27, 'magrth-road': 28, 'majestic': 29, 'malleshwaram': 30, 'marathahalli': 31, 'mathikere': 32, 'mg-road': 33, 'muneswara-nagar': 34, 'nagarathpete': 35, 'nagawara': 36, 'rajajinagar': 37, 'richmond-road': 38, 'rt-nagar': 39, 'sadashiv-nagar': 40, 'sanjay-nagar': 41, 'seshadripuram': 42, 'shanti-nagar': 43, 'shivaji-nagar': 44, 'stage-btm': 45, 'st-marks-road': 46, 'Commercial-street': 47, 'tavarekere': 48, 'town': 49, 'ulsoor': 50, 'vasanth-nagar': 51, 'vijay-nagar': 52, 'yeshwantpur': 53, 'adugodi': 54}
    if int(predictions1[0]) in location_dict.values():
        for key, value in location_dict.items():
            if value == int(predictions1[0]):
                print("Location is", key)
                break
    else:
        print("Unknown location")
    return key
key = ""
locan = locn(key)
