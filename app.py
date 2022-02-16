# importing the required libraries
import numpy as np
from flask import Flask, request, render_template
import joblib

# start flask
app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

# when the post method detect, then redirect to success function
@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # get form data
        cat_id = request.form.get('cat_id')
        age = request.form.get('age')
        gender = request.form.get('gender')
        profession = request.form.get('profession')
        views = request.form.get('views')
        if gender == 'female':
            gen = 0
        else:
            gen = 1

        if profession == 'student':
            prof = 0
        elif profession == 'working':
            prof = 1
        else:
            prof = 2

        # call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(cat_id, age, gen, prof, views)
            predict = np.round_(prediction, decimals = 4)
            return render_template('predict.html', prediction=predict)          # pass prediction to template
        except ValueError:
            return "Please Enter valid values"
        pass
    pass

def preprocessDataAndPredict(cat_id, age, gender, profession, views):
    test_data = [cat_id, age, gender, profession, views]                        # keep all inputs in array
    print(test_data)
    test_data = np.array(test_data)                                            # convert value data into numpy array
    test_data = test_data.reshape(1, -1)                                       # reshape array
    print(test_data)
    file = open("score_model.pkl", "rb")                                       # open file
    trained_model = joblib.load(file)                                          # load trained model
    prediction = trained_model.predict(test_data)                              # predict
    return prediction

if __name__ == '__main__':
    app.run(debug=True)